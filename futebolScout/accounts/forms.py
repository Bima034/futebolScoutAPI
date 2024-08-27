from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Pessoa


class UsuarioForm(UserCreationForm):
    dataNascimento = forms.DateField(label='Data de Nascimento', widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta():
        model = Pessoa
        fields = ['nome', 'username', 'dataNascimento']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields.pop('usable_password', None)

        self.fields['username'].label = 'Apelido'
        
        self.fields['nome'].label = 'Nome Completo'
        self.fields['dataNascimento'].label = 'Data de Nascimento'
        