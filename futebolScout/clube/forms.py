from django import forms
import requests
from .models import Clube
from federacao.models import Federacao


class ClubeCreaterForm(forms.ModelForm):
    response = requests.get('https://restcountries.com/v3.1/all')
    lista = []
    if response.status_code == 200:
        paises = response.json()
        lista_paises = [(pais.get("translations", {}).get("por", {}).get("common")) for pais in paises if pais.get("translations").get("por")]
    else:
        lista_paises = [('Brasil', 'Brasil')]
    lista_paises.sort()
    for pais_ in lista_paises:
        lista.append((pais_, pais_))
    nome = forms.CharField(label='Nome', max_length=100)
    sigla = forms.CharField(label='Sigla', max_length=5)
    pais = forms.ChoiceField(label='País de origem', choices=lista)
    federacao = forms.ModelMultipleChoiceField(label='Federações', queryset=Federacao.objects.all(), required=False)
    logoPath = forms.ImageField(label='Logo', required=False)
    treinador = forms.CharField(label='Treinador', max_length=100, required=False)
    presidente = forms.CharField(label='Presidente', max_length=100, required=False)
    estadio = forms.CharField(label='Estádio', max_length=250, required=False)
    fundacao = forms.DateField(label='Data de fundação', widget=forms.DateInput(attrs={'type': 'date'}))

    
    class Meta:
        model = Clube
        fields = ['nome', 'sigla', 'descricao', 'pais', 'federacao', 'logoPath', 'treinador', 'presidente', 'estadio', 'fundacao']
    
    def clean_sigla(self):
        return self.cleaned_data['sigla'].upper()