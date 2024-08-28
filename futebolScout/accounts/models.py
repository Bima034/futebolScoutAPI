from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Pessoa(User):
    nome = models.CharField(max_length=100)
    dataNascimento = models.DateField()
    apelido = models.CharField(max_length=100, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    