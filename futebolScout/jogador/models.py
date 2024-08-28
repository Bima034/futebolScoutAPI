from django.db import models

class Jogador(models.Model):
    POSICAO_CHOICES = [
        ('Goleiro', 'Goleiro'),
        ('Zagueiro', 'Zagueiro'),
        ('Lateral Esquerdo', 'Lateral Esquerdo'),
        ('Lateral Direito', 'Lateral Direito'),
        ('Volante', 'Volante'),
        ('Meio Campo', 'Meio Campo'),
        ('Meia atacante', 'Meia atacante'),
        ('Ponta esquerda', 'Ponta esquerda'),
        ('Ponta direita', 'Ponta direita'),
        ('Centroavante', 'Centroavante'),
        ('Atacante', 'Atacante'),
    ]
    MELHOR_PE_CHOICES = [
        ('Esquerdo', 'Esquerdo'),
        ('Direito', 'Direito'),
        ('Ambidestro', 'Ambidestro'),
    ]
    escolhas_avaliacao = [(i, str(i)) for i in range(11)] 
    nome_jogador = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=100)
    descricao = models.TextField(default='Não há descrição disponível para esse jogador') 
    altura = models.FloatField()
    melhor_pe = models.CharField(choices=MELHOR_PE_CHOICES, max_length=100)
    foto_path = models.CharField(max_length=250)
    fotoCapa_path = models.CharField(max_length=250)
    nota_media = models.FloatField(default=0.0, editable=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    
