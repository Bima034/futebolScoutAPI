from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .forms import CampeonatoForm
from .models import Campeonato
from accounts.models import Pessoa
from avaliacao.models import AvaliacaoCampeonato
from django.contrib.auth.decorators import login_required

# Create your views here.

def list(request):
    return render(request, 'campeonato/listCampeonato.html', {'campeonatos': Campeonato.objects.all()})

def add(request):
    if request.method == 'POST':
        form = CampeonatoForm(request.POST, request.FILES)
        if form.is_valid():
            campeonato =  form.save(commit=False)
            form.save(commit=True)
            
            return HttpResponseRedirect(f'/campeonato/detail/{campeonato.id}')
        else:
            print('Form Campeonato nao é válido')
            return render(request, "campeonato/addCampeonato.html", {'form': form})
        
    form = CampeonatoForm()
    return render(request, 'campeonato/addCampeonato.html', {'form': form})

@login_required
def detail(request, id):

    #AVALIANDO CAMPEONATO
    if request.method == 'POST':
        campeonato = Campeonato.objects.get(pk=id)
        valor = float(request.POST.get('nota', 0))

        try:
            pessoa = Pessoa.objects.get(pk=request.user.id)  
        except Pessoa.DoesNotExist:
            return render(request, 'campeonato/detailCampeonato.html', {'campeonato': campeonato, 'error': 'Perfil de Pessoa não encontrado.'})

        avaliacao_existente = AvaliacaoCampeonato.objects.filter(pessoa=pessoa, campeonato=campeonato).first()
        print(avaliacao_existente)

        if avaliacao_existente:
            avaliacao_existente.nota = valor
            avaliacao_existente.save()
        else:
            AvaliacaoCampeonato.objects.create(
                pessoa=pessoa,
                campeonato=campeonato,
                nota=valor
            )

        campeonato.refresh_from_db()
        return render(request, 'campeonato/detailCampeonato.html', {'campeonato': campeonato, 'valor': valor})

    if id:
        try:
            campeonato = Campeonato.objects.get(id=id)
        except Campeonato.DoesNotExist as error:
            return render(request, 'campeonato/detailCampeonato.html', {'error': error})
        return render(request, 'campeonato/detailCampeonato.html', {'campeonato': campeonato})
    else:
        return HttpResponseRedirect('/campeonato/', {'error': 'Campeonato não encontrado'})
    

def edit(request, id):
    campeonato = get_object_or_404(Campeonato, id=id)

    if request.method == 'POST':
        form = CampeonatoForm(request.POST, request.FILES, instance=campeonato)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/campeonato/detail/{campeonato.id}')
    else:
        form = CampeonatoForm(instance=campeonato)

    return render(request, 'campeonato/editCampeonato.html', {'form': form})

def delete(request, id):
    if request.method == 'POST':
        try:
            Campeonato.objects.get(id=id).delete()
            return HttpResponseRedirect('/campeonato/')
        except Campeonato.DoesNotExist:
            return HttpResponseRedirect('/campeonato/', {'error': 'Campeonato não encontrado'})
        
    return HttpResponseRedirect(f'/campeonato/detail/{id}')