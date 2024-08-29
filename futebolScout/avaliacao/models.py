from django.db import models
from accounts.models import Pessoa
from jogador.models import Jogador
from clube.models import Clube
from federacao.models import Federacao

class AvaliacaoJogador(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    jogador = models.ForeignKey(Jogador, on_delete=models.CASCADE)
    nota = models.FloatField()
    
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.atualizar_nota_media()

    def atualizar_nota_media(self):
        jogador = self.jogador
        avaliacoes = AvaliacaoJogador.objects.filter(jogador=jogador)
        nota_media = avaliacoes.aggregate(models.Avg('nota'))['nota__avg']
        nota_media_arredondada = round(nota_media or 0.0, 1)
        jogador.nota_media = nota_media_arredondada
        jogador.save()
        
class AvaliacaoClube(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    clube = models.ForeignKey(Clube, on_delete=models.CASCADE)
    nota = models.FloatField()
    
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.atualizar_nota_media()

    def atualizar_nota_media(self):
        clube = self.clube
        avaliacoes = AvaliacaoClube.objects.filter(clube=clube)
        nota_media = avaliacoes.aggregate(models.Avg('nota'))['nota__avg']
        nota_media_arredondada = round(nota_media or 0.0, 1)
        clube.nota_media = nota_media_arredondada
        clube.save()
        
class AvaliacaoFederacao(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    federacao = models.ForeignKey(Federacao, on_delete=models.CASCADE)
    nota = models.FloatField()
    
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.atualizar_nota_media()

    def atualizar_nota_media(self):
        federacao = self.federacao
        avaliacoes = AvaliacaoFederacao.objects.filter(federacao=federacao)
        nota_media = avaliacoes.aggregate(models.Avg('nota'))['nota__avg']
        nota_media_arredondada = round(nota_media or 0.0, 1)
        federacao.nota_media = nota_media_arredondada
        federacao.save()