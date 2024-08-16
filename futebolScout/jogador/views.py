from django.shortcuts import render

def dashboard(request):

    return render(request, "dashboard.html", {})

def listJogador(request):

    return render(request, "jogador/list.html", {})

