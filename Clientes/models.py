from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    comentario = models.CharField(max_length=250)