
from django.db import models

# Create your models here.
class Federacao(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=10)
    localidade = models.CharField(max_length=100)
    logo_path = models.ImageField(upload_to='imagens/federacao/', null=True, blank=True)
    presidente = models.CharField(max_length=100)
    fundacao = models.DateField(auto_now=False, auto_now_add=False)
    afiliada = models.ManyToManyField('self', symmetrical=False, blank=True, through='Afiliacoes', related_name='afiliacoes')
    
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nome

class Afiliacoes(models.Model):
    federacao = models.ForeignKey(Federacao, on_delete=models.CASCADE, related_name='federacao')
    federacao_afiliada = models.ForeignKey(Federacao, on_delete=models.CASCADE, related_name='federacao_afiliada')
    
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.federacao.nome} - {self.federacao_afiliada.nome}'