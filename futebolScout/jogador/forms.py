from django import forms
from .models import Jogador
from clube.models import Clube
import requests

class JogadorForm(forms.ModelForm):
    class Meta:
        model = Jogador
        fields = ['nome_jogador', 'nacionalidade', 'descricao', 'altura', 'melhor_pe', 'foto_path', 'fotoCapa_path']

    
    response = requests.get('https://restcountries.com/v3.1/all')
    lista = []
    if response.status_code == 200:
        paises = response.json()
        lista_paises = [(pais.get("translations", {}).get("por", {}).get("common")) for pais in paises if pais.get("translations").get("por")]
    else:
        lista_paises = [('Brasil', 'Brasil')]
    lista_paises.sort()
    for pais in lista_paises:
        lista.append((pais, pais))
    
    '''
    nome = forms.CharField(label='Nome', widget=forms.TextInput(attrs={'class': 'form-control'}))
    clube = forms.ModelChoiceField(
        queryset=Clube.objects.all(),
        label='Clube', 
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True,
        empty_label='Selecione o clube',
        
    )
    posicao = forms.ChoiceField(label='Posição', choices=Jogador.POSICAO_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    melhor_pe = forms.ChoiceField(label='Melhor Pé', choices=Jogador.MELHOR_PE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    dataNascimento = forms.DateField(label='Data de Nascimento', widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    foto_path = forms.ImageField(label='Foto', widget=forms.FileInput(attrs={'class': 'form-control mb-3'}))
    fotoCapa_path = forms.ImageField(label='Foto Capa', widget=forms.FileInput(attrs={'class': 'form-control mb-3'}))
    '''
    
    altura = forms.FloatField(label='Altura',widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: 1,80'}), max_value=2.5, min_value=1.0)
    nacionalidade = forms.ChoiceField(label='Nacionalidade', choices=lista, widget=forms.Select(attrs={'class': 'form-control'}))
    
    
        
    
