from django.shortcuts import render

def listFederacao(request):
    return render(request, "federacao/listFederacao.html", {})

def detailFederacao(request):
    return render(request, "federacao/detailFederacao.html", {})
