from django.db import models
from accounts.models import Pessoa
from federacao.models import Federacao
# Create your models here.

class Clube(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=5)
    pais = models.CharField(max_length=100)
    logo_path = models.ImageField(upload_to='clube/', null=True, blank=True)
    treinador = models.CharField(max_length=100, null=True, blank=True)
    presidente = models.CharField(max_length=100, null=True, blank=True)
    estadio = models.CharField(max_length=250, null=True, blank=True)
    fundacao = models.DateField(null=True, blank=True)
    federacoes = models.ManyToManyField(Federacao, blank=True)
    criado_por = models.ForeignKey(Pessoa, on_delete=models.SET_NULL, default=None, null=True, blank=True, auto_created=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)    
    descricao = models.TextField(null=True, blank=True)
    nota_media = models.FloatField(default=0.0, editable=False)
    
    def __str__(self):
        return self.nome
