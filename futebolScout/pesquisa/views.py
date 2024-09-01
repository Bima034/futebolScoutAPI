from django.shortcuts import render
from clube.models import Clube
from jogador.models import Jogador
from federacao.models import Federacao
from campeonato.models import Campeonato
from accounts.views import isGestor


# Create your views here.
def pesquisa(request):
    try:
        query = request.GET.get('query')
        print(query)
        resultado_pesquisa = []
        
        if query == None:
            return render(request, 'pesquisa/pesquisa.html', {'resultado_pesquisa': 'Nenhum resultado encontrado'})
        
        clube = Clube.objects.filter(nome__icontains=query)
        print(clube)
        for i in clube:
            clube_resultado = {
                'id': i.id,
                'nome': i.nome,
                'logo_path': i.logo_path,
                'nota_media': i.nota_media,
                'descricao': i.descricao,
                'url': 'clube'
            }
            resultado_pesquisa.append(clube_resultado)
            
        jogador = Jogador.objects.filter(nome_jogador__icontains=query)
        for i in jogador:
            jogador_resultado = {
                'id': i.id,
                'nome': i.nome_jogador,
                'logo_path': i.foto_path,
                'nota_media': i.nota_media,
                'descricao': i.descricao,
                'url': 'jogador'
            }
            resultado_pesquisa.append(jogador_resultado)
        
        federacao = Federacao.objects.filter(nome__icontains=query)
        for i in federacao:
            federacao_resultado = {
                'id': i.id,
                'nome': i.nome,
                'logo_path': i.logo_path,
                'nota_media': i.nota_media,
                'descricao': i.descricao,
                'url': 'federacao'
            }
            resultado_pesquisa.append(federacao_resultado)
        
        campeonato = Campeonato.objects.filter(nome__icontains=query)
        for i in campeonato:
            campeonato_resultado = {
                'id': i.id,
                'nome': i.nome,
                'logo_path': i.logo_path,
                'nota_media': i.nota_media,
                'descricao': i.descricao,
                'url': 'campeonato'
            }
            resultado_pesquisa.append(campeonato_resultado)
        resultado_pesquisa.sort(key=lambda x: (not x['nome'].lower().startswith(query.lower()), x['nome'].lower()))
        return render(request, 'pesquisa/pesquisa.html', {'resultado_pesquisa': resultado_pesquisa, 'isGestor': isGestor(request.user)})
        
    except Exception as error:
        print('erro:', error)
        return render(request, 'pesquisa/pesquisa.html', {'Deu erro': error, 'resultado_pesquisa': 'Nenhum resultado encontrado'})
