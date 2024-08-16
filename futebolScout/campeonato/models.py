from django.db import models
from clube.models import Clube
from federacao.models import Federacao

# Create your models here.

class Campeonato(models.Model):
    nome = models.CharField(max_length=100)
    nameRights = models.CharField()
    clubes = models.ManyToManyField(Clube, on_delete=models.CASCADE)
    federacao = models.ForeignKey(Federacao, on_delete=models.CASCADE)
    
    