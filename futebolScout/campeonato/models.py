from django.db import models

# Create your models here.

class Campeonato(models.Model):
    nome = models.CharField(max_length=100)
    nameRights = models.CharField()
    
    