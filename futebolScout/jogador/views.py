from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import JogadorForm
from django.http import HttpResponseRedirect
from .models import Jogador
from avaliacao.models import AvaliacaoJogador
from accounts.models import Pessoa


def dashboard(request):

    return render(request, "dashboard.html", {})


def listJogador(request):
    jogadores = Jogador.objects.all()
    return render(request, "jogador/listJogador.html", {"jogadores": jogadores})

@login_required
def detailJogador(request, jogador_id):

    #AVALIANDO
    if request.method == 'POST':
        jogador = Jogador.objects.get(pk=jogador_id)
        valor = float(request.POST.get('nota', 0))

        try:
            pessoa = Pessoa.objects.get(pk=request.user.id)  # Supondo que Pessoa tem um campo user referenciando User
        except Pessoa.DoesNotExist:
            # Lide com o caso onde a Pessoa não existe
            return render(request, 'jogador/detailJogador.html', {'jogador': jogador, 'error': 'Perfil de Pessoa não encontrado.'})

        # Tenta encontrar a avaliação existente
        avaliacao_existente = AvaliacaoJogador.objects.filter(pessoa=pessoa, jogador=jogador).first()

        if avaliacao_existente:
            # Atualiza a avaliação existente
            avaliacao_existente.nota = valor
            avaliacao_existente.save()
        else:
            # Cria uma nova avaliação
            AvaliacaoJogador.objects.create(
                pessoa=pessoa,
                jogador=jogador,
                nota=valor
            )

        # Atualiza o objeto 'jogador' com a nova média
        jogador.refresh_from_db()

        return render(request, 'jogador/detailJogador.html', {'jogador': jogador, 'valor': valor})

    jogador = Jogador.objects.get(pk=jogador_id)
    return render(request, "jogador/detailJogador.html", {"jogador": jogador })

def addJogador(request):
    
    if request.method == 'POST':
        form = JogadorForm(request.POST)
        if form.is_valid():
            jogador =  form.save(commit=False)
            form.save(commit=True)
            
            return HttpResponseRedirect(f'/jogador/')
        else:
            print('nao eh válido')
            return render(request, "jogador/addJogador.html", {'form': form})
        
    form = JogadorForm()
    return render(request, "jogador/addJogador.html", {'form': form})

def editJogador(request, jogador_id):

    jogador = Jogador.objects.get(pk=jogador_id)

    if request.method == "POST":
        
        form = JogadorForm(request.POST, instance=jogador)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/jogador/')

    else:
        form = JogadorForm(instance=jogador)
    
    return render(request, 'jogador/editJogador.html', {'form': form})

def deleteJogador(request, jogador_id):

    Jogador.objects.get(pk=jogador_id).delete()
    return HttpResponseRedirect('/jogador/')

