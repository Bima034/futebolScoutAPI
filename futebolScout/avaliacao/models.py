from django.db import models

# Create your models here.
class Avaliacao(models.Model):
    jogador = models.ForeignKey('jogador.Jogador', on_delete=models.CASCADE)
    usuario = models.ForeignKey('accounts.Pessoa', on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    estrelas = models.IntegerField()
    comentario = models.TextField()