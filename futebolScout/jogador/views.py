from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import JogadorCreaterForm
from django.http import HttpResponseRedirect
from .models import Jogador

@login_required
def dashboard(request):

    return render(request, "dashboard.html", {})


def listJogador(request):

    return render(request, "jogador/listJogador.html", {})



def detailJogador(request, id):
    if id:
        jogador = Jogador.objects.get(id=id)
        return render(request, "jogador/detailJogador.html", {'jogador': jogador})
    else:
        return HttpResponseRedirect('/jogador/list/')


def addJogador(request):
    if request.method == 'POST':
        form = JogadorCreaterForm(request.POST)
        if form.is_valid():
            jogador =  form.save(commit=False)
            form.save(commit=True)
            
            return HttpResponseRedirect(f'/jogador/detail/{jogador.id}')
        else:
            print('nao eh válido')
            return render(request, "jogador/addJogador.html", {'form': form})
        
    form = JogadorCreaterForm()
    return render(request, "jogador/addJogador.html", {'form': form})

