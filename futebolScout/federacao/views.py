from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')

def detailFederacao(request):
    return render(request, 'detailFederacao.html')

def listFederacao(request):
    return render(request, 'listFederacao.html')