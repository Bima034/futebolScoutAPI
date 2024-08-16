from django.db import models
from accounts.models import Pessoa
# Create your models here.
class Jogador(Pessoa):
    nacionalidade = models.CharField(max_length=100)
    descricao = models.TextField()
    altura = models.FloatField()
    melhor_pe = models.CharField(choices=("Esquerdo, Direito, Ambidestro"), max_length=100)
    foto_path = models.CharField(max_length=250)
    
    def __str__(self):
        return self.nome