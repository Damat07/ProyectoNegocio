from django.db import models

# Create your models here.

class Empleado(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    puesto = models.CharField(max_length=20)