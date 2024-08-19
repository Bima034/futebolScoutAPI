from django.db import models
# Create your models here.
class Jogador(models.Model):
    escolhas_avaliacao = [(i, str(i)) for i in range(11)] 
    
    nome_jogador = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=100)
    descricao = models.TextField()
    altura = models.FloatField()
    melhor_pe = models.CharField(choices=[('Esquerdo', 'Esquerdo'), ('Direito', 'Direito'), ('Ambidestro', 'Ambidestro')], max_length=100)
    foto_path = models.CharField(max_length=250)
    fotoCapa_path = models.CharField(max_length=250)
    avaliacao = models.IntegerField(choices=escolhas_avaliacao, default=0)
    
    