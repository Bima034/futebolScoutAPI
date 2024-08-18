from django.shortcuts import render, redirect
from .forms import UsuarioForm

# Create your views here.

def createUser(request):
    
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('login')
        
    else:
        form = UsuarioForm()
        
        
    return render(request, 'accounts/criarUsuario.html', {'form':form})
        
    