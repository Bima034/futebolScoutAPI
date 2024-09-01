from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import JogadorForm
from django.http import HttpResponseRedirect
from .models import Jogador
from clube.models import Clube
from federacao.models import Federacao
from campeonato.models import Campeonato
from avaliacao.models import AvaliacaoJogador
from accounts.models import Pessoa
from accounts.views import isGestor

@login_required
def dashboard(request):
    top_jogadores = Jogador.objects.order_by('-nota_media')[:3]
    top_clubes = Clube.objects.order_by('-nota_media')[:3]
    top_federacoes = Federacao.objects.order_by('-nota_media')[:3]
    top_campeonatos = Campeonato.objects.order_by('-nota_media')[:3]

    contexto = {
        'top_jogadores': top_jogadores,
        'top_clubes': top_clubes,
        'top_federacoes': top_federacoes,
        'top_campeonatos': top_campeonatos,
        'isGestor': isGestor(request.user)
    }

    return render(request, "dashboard.html", contexto)

@login_required
def listJogador(request):
    jogadores = Jogador.objects.all()
    return render(request, "jogador/listJogador.html", {"jogadores": jogadores, 'isGestor': isGestor(request.user)})

@login_required
def detailJogador(request, jogador_id):

    #AVALIANDO JOGADOR
    if request.method == 'POST':
        jogador = Jogador.objects.get(pk=jogador_id)
        valor = float(request.POST.get('nota', 0))

        try:
            pessoa = Pessoa.objects.get(pk=request.user.id)  
        except Pessoa.DoesNotExist:
            return render(request, 'jogador/detailJogador.html', {'jogador': jogador, 'error': 'Perfil de Pessoa não encontrado.'})

        avaliacao_existente = AvaliacaoJogador.objects.filter(pessoa=pessoa, jogador=jogador).first()

        if avaliacao_existente:
            avaliacao_existente.nota = valor
            avaliacao_existente.save()
        else:
            AvaliacaoJogador.objects.create(
                pessoa=pessoa,
                jogador=jogador,
                nota=valor
            )

        jogador.refresh_from_db()
        return render(request, 'jogador/detailJogador.html', {'jogador': jogador, 'valor': valor})

    jogador = Jogador.objects.get(pk=jogador_id)
    return render(request, "jogador/detailJogador.html", {"jogador": jogador })

@login_required
def addJogador(request):
    
    if request.method == 'POST':
        form = JogadorForm(request.POST, request.FILES)
        if form.is_valid():
            jogador =  form.save(commit=False)
            form.save(commit=True)
            
            return HttpResponseRedirect(f'/jogador/')
        else:
            print('nao eh válido')
            return render(request, "jogador/addJogador.html", {'form': form})
        
    form = JogadorForm()
    return render(request, "jogador/addJogador.html", {'form': form})

@login_required
def editJogador(request, jogador_id):
    
    jogador = get_object_or_404(Jogador, id=jogador_id)

    if request.method == "POST":
        
        form = JogadorForm(request.POST, request.FILES, instance=jogador)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/jogador/')

    else:
        form = JogadorForm(instance=jogador)
    
    return render(request, 'jogador/editJogador.html', {'form': form})

@login_required
def deleteJogador(request, jogador_id):
    if request.method == 'POST':
        try:
            Jogador.objects.get(pk=jogador_id).delete()
            return HttpResponseRedirect('/jogador/')
        except Jogador.DoesNotExist:
            return HttpResponseRedirect('/jogador/', {'error': 'Jogador não encontrado'})

    return HttpResponseRedirect(f'/jogador/detail/{jogador_id}')