from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import JogadorForm
from django.http import HttpResponseRedirect
from .models import Jogador

def dashboard(request):

    return render(request, "dashboard.html", {})


def listJogador(request):
    jogadores = Jogador.objects.all()
    return render(request, "jogador/listJogador.html", {"jogadores": jogadores})

def detailJogador(request, jogador_id):
    jogador = Jogador.objects.get(pk=jogador_id)
    return render(request, "jogador/detailJogador.html", {"jogador": jogador })

def addJogador(request):
    
    if request.method == 'POST':
        form = JogadorForm(request.POST)
        if form.is_valid():
            jogador =  form.save(commit=False)
            form.save(commit=True)
            
            return HttpResponseRedirect(f'/jogador/list/')
        else:
            print('nao eh válido')
            return render(request, "jogador/addJogador.html", {'form': form})
        
    form = JogadorForm()
    return render(request, "jogador/addJogador.html", {'form': form})

def editJogador(request, jogador_id):

    jogador = Jogador.objects.get(pk=jogador_id)

    if request.method == "POST":
        
        form = JogadorForm(request.POST, instance=jogador)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/jogador/')

    else:
        form = JogadorForm(instance=jogador)
    
    return render(request, 'jogador/editJogador.html', {'form': form})

def deleteJogador(request, jogador_id):

    Jogador.objects.get(pk=jogador_id).delete()
    return HttpResponseRedirect('/jogador/list/')

