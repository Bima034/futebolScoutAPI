from django import forms
from .models import Federacao
import requests

class FederacaoCreaterForm(forms.ModelForm):
    localidade = forms.ChoiceField(label='Localidade')
    fundacao = forms.DateField(label='Data de Fundação', widget=forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'), input_formats=['%Y-%m-%d'])
    afiliada = forms.ModelMultipleChoiceField(label='Afiliada', queryset=Federacao.objects.all(), required=False)
    
    class Meta:
        model = Federacao
        fields = '__all__'
        exclude = ['comentarios']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Inicializa lista de opções para o campo de localidade
        lista_paises = []
        try:
            response = requests.get('https://restcountries.com/v3.1/all')
            if response.status_code == 200:
                paises = response.json()
                lista_paises = [(pais.get("translations", {}).get("por", {}).get("common")) for pais in paises if pais.get("translations").get("por")]
            else:
                lista_paises = ['Brasil']
        except requests.exceptions.RequestException:
            lista_paises = ['Brasil']
        
        lista_paises.sort()
        self.fields['localidade'].choices = [(pais_, pais_) for pais_ in lista_paises]
