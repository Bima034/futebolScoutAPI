from django import forms
import requests
from .models import Clube
from federacao.utils import query_set_federacao_pais


class ClubeCreaterForm(forms.Form):
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
    nome = forms.CharField(label='Nome', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    sigla = forms.CharField(label='Sigla', max_length=3, widget=forms.TextInput(attrs={'class': 'form-control'}))
    pais = forms.ChoiceField(label='País de origem', choices=lista, widget=forms.Select(attrs={'class': 'form-control'}))
    value_pais = pais.choices[0][0]
    federacao = forms.ModelChoiceField(
        queryset=query_set_federacao_pais(pais=value_pais),
        label='Federação',
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label='Selecione a federação'
        )
    logoPath = forms.ImageField(label='Logo', widget=forms.FileInput(attrs={'class': 'form-control mb-3'}))
    
    
    class Meta:
        model = Clube
        fields = ['nome', 'sigla', 'pais', 'federacao']