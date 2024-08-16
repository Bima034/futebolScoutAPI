from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Pessoa(User):
    nome = models.CharField(max_length=100)
    dataNascimento = models.DateField()
    

class Usuario(Pessoa):
    apelido = models.CharField(max_length=100)