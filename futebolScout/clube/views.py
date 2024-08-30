from django.shortcuts import render
from .forms import ClubeCreaterForm
from django.http import HttpResponseRedirect
from .models import Clube
from accounts.models import Pessoa
from avaliacao.models import AvaliacaoClube
from django.contrib.auth.decorators import login_required

# Create your views here.
def list(request):
    return render(request, 'clube/listClube.html', {'clubes': Clube.objects.all()})

def add(request):
    if request.method == 'POST':
        form = ClubeCreaterForm(request.POST)
        if form.is_valid():
            clube =  form.save(commit=False)
            form.save(commit=True)
            
            return HttpResponseRedirect(f'/clube/detail/{clube.id}')
        else:
            print('Form Clube nao é válido')
            return render(request, "clube/addClube.html", {'form': form})
        
    form = ClubeCreaterForm()
    return render(request, 'clube/addClube.html', {'form': form})

@login_required
def detail(request, id):

    #AVALIANDO CLUBE
    if request.method == 'POST':
        clube = Clube.objects.get(pk=id)
        valor = float(request.POST.get('nota', 0))

        try:
            pessoa = Pessoa.objects.get(pk=request.user.id)  
        except Pessoa.DoesNotExist:
            return render(request, 'clube/detailClube.html', {'clube': clube, 'error': 'Perfil de Pessoa não encontrado.'})

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
        return render(request, 'clube/detailClube.html', {'clube': clube, 'valor': valor})

    if id:
        try:
            clube = Clube.objects.get(id=id)
        except Clube.DoesNotExist as error:
            return render(request, 'clube/detailClube.html', {'error': error})
        return render(request, 'clube/detailClube.html', {'clube': clube})
    else:
        return HttpResponseRedirect('/clube/', {'error': 'Clube não encontrado'})
        
def edit(request, id):
    if id:
        clube = Clube.objects.get(id=id)
        form = ClubeCreaterForm(request.POST or None, instance=clube)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/clube/detail/{clube.id}')
        return render(request, 'clube/editClube.html', {'form': form})
    else:
        return HttpResponseRedirect('/clube/', {'error': 'Clube não encontrado'})
        
def delete(request, id):
    if request.method == 'POST':
        try:
            clube = Clube.objects.get(id=id)
            clube.delete()
            return HttpResponseRedirect('/clube/')
        except Clube.DoesNotExist:
            return HttpResponseRedirect('/clube/', {'error': 'Clube não encontrado'})
    else: 
        return HttpResponseRedirect(f'/clube/detail/{id}')