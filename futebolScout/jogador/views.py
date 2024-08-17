from django.shortcuts import render
from django.contrib.auth.decorators import login_required

#@login_required
def dashboard(request):

    return render(request, "dashboard.html", {})

def listJogador(request):

    return render(request, "jogador/listJogador.html", {})

def detailJogador(request):

    return render(request, "jogador/detailJogador.html", {})

def addJogador(request):

    return render(request, "jogador/addJogador.html", {})

