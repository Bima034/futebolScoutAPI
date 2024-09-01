from django.shortcuts import render, redirect
from .forms import UsuarioForm
from django.contrib.auth.models import Group

def isGestor(user):
    return user.groups.filter(name='Gestores').exists()

def createUser(request):
    
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)

            alunos_group = Group.objects.get(name='Torcedores')
            user.groups.add(alunos_group)
            
            user.save()

            return redirect('login')
        
    else:
        form = UsuarioForm()
        
        
    return render(request, 'accounts/criarUsuario.html', {'form':form})
        
    