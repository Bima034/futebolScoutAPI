from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Pessoa

class PessoaForm(UserCreationForm):
    class Meta:
        model = Pessoa
        fields = [
            'username', 
            'email', 
            'password1', 
            'password2', 
            'nome', 
            'dataNascimento', 
            'apelido',
            'grupo'
        ]
        widgets = {
            'dataNascimento': forms.DateInput(attrs={'type': 'date'})
        }