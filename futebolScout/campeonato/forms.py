from django import forms
from .models import Campeonato

class CampeonatoForm(forms.ModelForm):
    
    logo_path = forms.ImageField(label='Logo', required=False)
    class Meta:
        model = Campeonato
        fields = '__all__'
        
   