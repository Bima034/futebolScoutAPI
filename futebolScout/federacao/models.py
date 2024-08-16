from django.db import models

# Create your models here.
class Federacao(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=3)
    localidade = models.CharField(max_length=100)
    logo_path = models.CharField(max_length=250)
    presidente = models.CharField(max_length=100)
    fundacao = models.DateField(auto_now=False, auto_now_add=False)
    afiliada = models.ManyToManyField('self', through='federacao_afiliacao', symmetrical=False)
    
    def __str__(self):
        return self.nome