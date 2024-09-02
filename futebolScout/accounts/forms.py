from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Pessoa


class UsuarioForm(UserCreationForm):
    dataNascimento = forms.DateField(label='Data de Nascimento', widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta():
        model = Pessoa
        fields = ['nome', 'username', 'email', 'dataNascimento']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields.pop('usable_password', None)

        self.fields['username'].label = 'Nome de usuário'
        
        self.fields['nome'].label = 'Nome Completo'
        self.fields['dataNascimento'].label = 'Data de Nascimento'
        self.fields['email'].required = True
        