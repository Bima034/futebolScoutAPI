from rest_framework import viewsets
from .models import Clube
from .serializers import ClubeSerializer
from .permissions import IsAuthenticatedWithJWT
class ClubeViewSet(viewsets.ModelViewSet):
    
    permission_classes = [IsAuthenticatedWithJWT]
    
    queryset = Clube.objects.all()
    serializer_class = ClubeSerializer

'''
from django.shortcuts import render, get_object_or_404
from .forms import ClubeCreaterForm
from django.http import HttpResponseRedirect
from .models import Clube
from accounts.models import Pessoa
from avaliacao.models import AvaliacaoClube
from django.contrib.auth.decorators import login_required
from accounts.views import isGestor, isTorcedor


# Create your views here.
def listClube(request):
    return render(request, 'clube/listClube.html', {'clubes': Clube.objects.all(), 'isGestor': isGestor(request.user)})

@login_required
def addClube(request):
    if request.method == 'POST':
        form = ClubeCreaterForm(request.POST, request.FILES)
        if form.is_valid():
            clube =  form.save(commit=False)
            clube.save()
            if form.cleaned_data['federacoes'] is not None:
                form.save_m2m()
            return HttpResponseRedirect(f'/clube/detail/{clube.id}')
        else:
            print('Form Clube nao é válido')
            return render(request, "clube/addClube.html", {'form': form})
        
    form = ClubeCreaterForm()
    return render(request, 'clube/addClube.html', {'form': form})

def detailClube(request, id):

    #AVALIANDO CLUBE
    if request.method == 'POST':
        clube = Clube.objects.get(pk=id)
        valor = float(request.POST.get('nota', 0))

        try:
            pessoa = Pessoa.objects.get(pk=request.user.id)  
        except Pessoa.DoesNotExist:
            return render(request, 'clube/detailClube.html', {'clube': clube, 'error': 'Perfil de Pessoa não encontrado.', 'isTorcedor': isTorcedor(request.user)})

        avaliacao_existente = AvaliacaoClube.objects.filter(pessoa=pessoa, clube=clube).first()

        if avaliacao_existente:
            avaliacao_existente.nota = valor
            avaliacao_existente.save()
        else:
            AvaliacaoClube.objects.create(
                pessoa=pessoa,
                clube=clube,
                nota=valor
            )

        clube.refresh_from_db()
        return render(request, 'clube/detailClube.html', {'clube': clube, 'valor': valor, 'isTorcedor': isTorcedor(request.user)})

    if id:
        try:
            clube = Clube.objects.get(id=id)
        except Clube.DoesNotExist as error:
            return render(request, 'clube/detailClube.html', {'error': error, 'isTorcedor': isTorcedor(request.user)})
        return render(request, 'clube/detailClube.html', {'clube': clube, 'isTorcedor': isTorcedor(request.user)})
    else:
        return HttpResponseRedirect('/clube/', {'error': 'Clube não encontrado', 'isTorcedor': isTorcedor(request.user)})

@login_required       
def editClube(request, id):
    clube = get_object_or_404(Clube, id=id)
    print(clube.fundacao)
    
    if request.method == 'POST':
        form = ClubeCreaterForm(request.POST, request.FILES, instance=clube)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/clube/detail/{clube.id}')
    else:
        form = ClubeCreaterForm(instance=clube)
        
    return render(request, 'clube/editClube.html', {'form': form})

@login_required   
def deleteClube(request, id):
    if request.method == 'POST':
        try:
            clube = Clube.objects.get(id=id)
            clube.delete()
            return HttpResponseRedirect('/clube/')
        except Clube.DoesNotExist:
            return HttpResponseRedirect('/clube/', {'error': 'Clube não encontrado'})
    else: 
        return HttpResponseRedirect(f'/clube/detail/{id}')'
'''