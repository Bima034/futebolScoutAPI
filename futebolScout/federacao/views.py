from django.shortcuts import render
from .forms import FederacaoCreaterForm
from django.http import HttpResponseRedirect
from .models import Federacao


def listFederacao(request):
    return render(request, "federacao/listFederacao.html", {})

def detailFederacao(request, id):
    federacao = Federacao.objects.get(id=id)
    return render(request, "federacao/detailFederacao.html", {'federacao': federacao})

def add(request):
    if request.method == 'GET':
        form = FederacaoCreaterForm()
        return render(request, "federacao/addFederacao.html", {'form': form})
    elif request.method == 'POST':
        form = FederacaoCreaterForm(request.POST)
        if form.is_valid():
            federacao =  form.save(commit=False)
            form.save(commit=True)
            
            return HttpResponseRedirect(f'/federacao/detail/{federacao.id}')
        