from django.db import models

class Paleta(models.Model):
    marca = models.CharField(max_length=30)
    descripcion = models.TextField()
    anio = models.IntegerField()