from django import forms
from .models import Federacao

class FederacaoCreaterForm(forms.ModelForm):
    class Meta:
        model = Federacao
        fields = '__all__'