from django.shortcuts import render, redirect
from .forms import UsuarioForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

def isGestor(user):
    return user.groups.filter(name='Gestores').exists()

def createUser(request):
    
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        
        if form.is_valid():
            user = form.save()

            alunos_group, created = Group.objects.get_or_create(name='Torcedores')
            user.groups.add(alunos_group)
            
            user.save()

            return redirect('login')
        
    else:
        form = UsuarioForm()
        
        
    return render(request, 'accounts/criarUsuario.html', {'form':form})

@login_required
def telaPerfil(request):
    # print('User: ', request.user)
    # pessoa = request.user
    # pessoa = pessoa.pessoa
    # print(pessoa.__dict__)
    # retorno = {
    #     'nome': pessoa.nome,
    #     'apelido': pessoa.username,
    #     'dataNascimento': pessoa.dataNascimento,
    #     'email': pessoa.email
    # }
    return render(request, 'accounts/telaPerfil.html')