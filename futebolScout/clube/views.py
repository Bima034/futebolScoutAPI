from django.shortcuts import render
from .forms import ClubeCreaterForm
from django.http import HttpResponseRedirect
from .models import Clube

# Create your views here.

def dashboard(request):
    return render(request, 'dashboardClube.html')

def list(request):
    return render(request, 'clube/listClube.html')

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

def detail(request, id):
    if id:
        clube = Clube.objects.get(id=id)
        return render(request, 'clube/detailClube.html', {'clube': clube})
    else:
        return HttpResponseRedirect('/clube/list/')