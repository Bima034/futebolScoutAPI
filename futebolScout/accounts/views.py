from django.shortcuts import render, HttpResponse
from .forms import UsuarioForm

# Create your views here.

def createUser(request):
    
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        
        if form.is_valid():
            form.save()
        
    else:
        form = UsuarioForm()
        
        
    return render(request, 'accounts/criarUsuario.html', {'form':form})
        
    