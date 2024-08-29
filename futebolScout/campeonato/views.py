from django.shortcuts import render, HttpResponseRedirect
from .forms import CampeonatoForm
from .models import Campeonato

# Create your views here.

def list(request):
    return render(request, 'campeonato/listCampeonato.html', {'campeonatos': Campeonato.objects.all()})

def add(request):
    if request.method == 'POST':
        form = CampeonatoForm(request.POST)
        if form.is_valid():
            campeonato =  form.save(commit=False)
            form.save(commit=True)
            
            return HttpResponseRedirect(f'/campeonato/detail/{campeonato.id}')
        else:
            print('Form Campeonato nao é válido')
            return render(request, "campeonato/addCampeonato.html", {'form': form})
        
    form = CampeonatoForm()
    return render(request, 'campeonato/addCampeonato.html', {'form': form})

def detail(request, id):
    if id:
        try:
            campeonato = Campeonato.objects.get(id=id)
        except Campeonato.DoesNotExist as error:
            return render(request, 'campeonato/detailCampeonato.html', {'error': error})
        return render(request, 'campeonato/detailCampeonato.html', {'campeonato': campeonato})
    else:
        return HttpResponseRedirect('/campeonato/list/', {'error': 'Campeonato não encontrado'})
    

def edit(request, id):
    if id:
        campeonato = Campeonato.objects.get(id=id)
        form = CampeonatoForm(request.POST or None, instance=campeonato)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/campeonato/detail/{campeonato.id}')
        return render(request, 'campeonato/editCampeonato.html', {'form': form})
    else:
        return HttpResponseRedirect('/campeonato/list/', {'error': 'Campeonato não encontrado'})

def delete(request, id):
    if request.method == 'POST':
        try:
            Campeonato.objects.get(id=id).delete()
            return HttpResponseRedirect('/campeonato/list/')
        except Campeonato.DoesNotExist:
            return HttpResponseRedirect('/campeonato/list/', {'error': 'Campeonato não encontrado'})
        
    return HttpResponseRedirect(f'/campeonato/detail/{id}')