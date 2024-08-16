from django.db import models
from accounts.models import Pessoa
# Create your models here.
class Clube(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=3)
    pais = models.CharField(max_length=100)
    logo_path = models.CharField(max_length=250)
    treinador = models.ForeignKey(Pessoa)
    presidente = models.ForeignKey(Pessoa)
    estadio = models.CharField(max_length=250)
    fundacao = models.DateField(auto_now=False, auto_now_add=False)
    jogadores =    

    def __str__(self):
        return self.nome