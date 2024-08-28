from django.shortcuts import render
from .forms import FederacaoCreaterForm
from django.http import HttpResponseRedirect, HttpResponse
from .models import Federacao


def listFederacao(request):
    federacoes = Federacao.objects.all()
    return render(request, "federacao/listFederacao.html", {'federacoes': federacoes})

def detailFederacao(request, id_federacao):
    if request.method == 'GET':
        federacao = Federacao.objects.get(id=id_federacao)
        print(federacao.afiliada.all())
        return render(request, "federacao/detailFederacao.html", {'federacao': federacao})
    return HttpResponse('Método não permitido', status=405)

def add(request):
    if request.method == 'POST':
        form = FederacaoCreaterForm(request.POST)
        if form.is_valid():
            federacao =  form.save(commit=False)
            federacao.save()
            if form.cleaned_data['afiliada'] is not None:
                form.save_m2m()
            return HttpResponseRedirect(f'/federacao/detail/{federacao.id}')
    form = FederacaoCreaterForm()
    return render(request, "federacao/addFederacao.html", {'form': form})

def delete(request, id_federacao):
    if request.method == 'POST':
        federacao = Federacao.objects.get(id=id_federacao)
        federacao.delete()
        return HttpResponseRedirect('/federacao/list/')
    return HttpResponse('Método não permitido', status=405)

def edit(request, id_federacao):
    if request.method == 'GET':
        federacao = Federacao.objects.get(id=id_federacao)
        form = FederacaoCreaterForm(instance=federacao)
        return render(request, "federacao/editFederacao.html", {'form': form})
    elif request.method == 'POST':
        federacao = Federacao.objects.get(id=id_federacao)
        form = FederacaoCreaterForm(request.POST, instance=federacao)
        if form.is_valid():
            federacao =  form.save(commit=False)
            federacao.save()
            
            if form.cleaned_data['afiliada'] is not None:
                form.save_m2m()
            
            return HttpResponseRedirect(f'/federacao/detail/{federacao.id}')
        else:
            return render(request, "federacao/editFederacao.html", {'form': form})
    return HttpResponse('Método não permitido', status=405)

