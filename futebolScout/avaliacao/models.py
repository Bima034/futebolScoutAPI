from django.db import models
from accounts.models import Pessoa
from jogador.models import Jogador


# Create your models here.
class Avaliacao(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    jogador = models.ForeignKey(Jogador, on_delete=models.CASCADE)
    nota = models.FloatField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)