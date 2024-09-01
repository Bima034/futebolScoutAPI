
from django.db import models
from clube.models import Clube
from federacao.models import Federacao

# Create your models here.

class Campeonato(models.Model):
    nome = models.CharField(max_length=100)
    nameRights = models.CharField(max_length=100)
    clubes = models.ManyToManyField(Clube)
    federacao = models.ForeignKey(Federacao, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    logo_path = models.ImageField(upload_to='campeonato/', null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)
    nota_media = models.FloatField(default=0.0, editable=False)


    