from django.db import models

class Ficha(models.Model):

    nome = models.CharField(max_length=50, null = False)
    classe = models.CharField(max_length=20, null = False)
    raca = models.CharField(max_length=20, null = False)
    equipamento = models.CharField(max_length=20, null = False)
