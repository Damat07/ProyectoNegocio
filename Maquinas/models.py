from django.db import models

# Create your models here.

class Maquina(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=40)
    año = models.IntegerField()
    descripcion = models.CharField(max_length=250)
