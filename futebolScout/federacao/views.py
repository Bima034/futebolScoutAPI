from rest_framework import viewsets
from .models import Federacao
from .serializers import FederacaoSerializer
from .permissions import IsAuthenticatedWithJWT
class FederacaoViewSet(viewsets.ModelViewSet):
    
    permission_classes = [IsAuthenticatedWithJWT]
    
    queryset = Federacao.objects.all()
    serializer_class = FederacaoSerializer
    
    
'''
from django.shortcuts import render, get_object_or_404
from .forms import FederacaoCreaterForm
from django.http import HttpResponseRedirect, HttpResponse
from .models import Federacao
from accounts.models import Pessoa
from avaliacao.models import AvaliacaoFederacao
from django.contrib.auth.decorators import login_required
from accounts.views import isGestor, isTorcedor

def listFederacao(request):
    return render(request, "federacao/listFederacao.html", {'federacoes': Federacao.objects.all(), 'isGestor': isGestor(request.user)})

def detailFederacao(request, id_federacao):

    #AVALIANDO FEDERAÇÃO
    if request.method == 'POST':
        if request.user.is_authenticated:
            federacao = Federacao.objects.get(pk=id_federacao)
            valor = float(request.POST.get('nota', 0))

            try:
                pessoa = Pessoa.objects.get(pk=request.user.id)  
            except Pessoa.DoesNotExist:
                return render(request, 'federacao/detailFederacao.html', {'federacao': federacao, 'error': 'Perfil de Pessoa não encontrado.', 'isTorcedor': isTorcedor(request.user)})

            avaliacao_existente = AvaliacaoFederacao.objects.filter(pessoa=pessoa, federacao=federacao).first()

            if avaliacao_existente:
                avaliacao_existente.nota = valor
                avaliacao_existente.save()
            else:
                AvaliacaoFederacao.objects.create(
                    pessoa=pessoa,
                    federacao=federacao,
                    nota=valor
                )

            federacao.refresh_from_db()
            return render(request, 'federacao/detailFederacao.html', {'federacao': federacao, 'valor': valor, 'isTorcedor': isTorcedor(request.user)})
        else:
            return HttpResponseRedirect(f'/accounts/login/', {'isTorcedor': isTorcedor(request.user)})

    if request.method == 'GET':
        federacao = Federacao.objects.get(id=id_federacao)
        print(federacao.afiliada.all())
        return render(request, "federacao/detailFederacao.html", {'federacao': federacao, 'isTorcedor': isTorcedor(request.user)})
    return HttpResponse('Método não permitido', status=405)

@login_required
def addJogador(request):
    if request.method == 'POST':
        form = FederacaoCreaterForm(request.POST, request.FILES)
        if form.is_valid():
            federacao =  form.save(commit=False)
            federacao.save()
            if form.cleaned_data['afiliada'] is not None:
                form.save_m2m()
            return HttpResponseRedirect(f'/federacao/detail/{federacao.id}')
    form = FederacaoCreaterForm()
    return render(request, "federacao/addFederacao.html", {'form': form})

@login_required
def deleteJogador(request, id_federacao):
    if request.method == 'POST':
        try:
            federacao = Federacao.objects.get(id=id_federacao)
            federacao.delete()
            return HttpResponseRedirect('/federacao/')
        except Federacao.DoesNotExist:
            return HttpResponseRedirect('/federacao/', {'error': 'Federação não encontrada'})

    return HttpResponseRedirect(f'/federacao/detail/{id_federacao}')

@login_required
def editJogador(request, id_federacao):
    federacao = get_object_or_404(Federacao, id=id_federacao)
    
    if request.method == 'GET':
        form = FederacaoCreaterForm(instance=federacao)
        return render(request, "federacao/editFederacao.html", {'form': form})
    elif request.method == 'POST':
        form = FederacaoCreaterForm(request.POST, request.FILES, instance=federacao)
        if form.is_valid():
            federacao =  form.save(commit=False)
            federacao.save()
            
            if form.cleaned_data['afiliada'] is not None:
                form.save_m2m()
            
            return HttpResponseRedirect(f'/federacao/detail/{federacao.id}')
        else:
            return render(request, "federacao/editFederacao.html", {'form': form})
    return HttpResponse('Método não permitido', status=405)

'''