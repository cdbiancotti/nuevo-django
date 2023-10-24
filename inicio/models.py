from django.db import models

class Paleta(models.Model):
    marca = models.CharField(max_length=30)
    descripcion = models.TextField()
    anio = models.IntegerField()
    
    def __str__(self):
        return f'{self.id} - {self.marca} - {self.anio}'