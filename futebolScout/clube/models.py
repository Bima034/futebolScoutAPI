from django.db import models
from accounts.models import Pessoa
from jogador.models import Jogador
from federacao.models import Federacao
# Create your models here.

class Clube(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=3)
    pais = models.CharField(max_length=100)
    logo_path = models.CharField(max_length=250)
    treinador = models.CharField(max_length=100)
    presidente = models.CharField(max_length=100)
    jogadores =  models.ManyToManyField(Jogador)
    estadio = models.CharField(max_length=250)
    fundacao = models.DateField(auto_now=False, auto_now_add=False)
    federacao = models.ForeignKey(Federacao, on_delete=models.SET_NULL, default=None, null=True, blank=True)
    criado_por = models.ForeignKey(Pessoa, on_delete=models.SET_NULL, default=None, null=True, blank=True)
    
    def __str__(self):
        return self.nome

