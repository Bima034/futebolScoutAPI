from django import forms
from .models import Campeonato

class CampeonatoForm(forms.ModelForm):
    class Meta:
        model = Campeonato
        fields = '__all__'