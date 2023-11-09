from django.db import models
from ckeditor.fields import RichTextField

class Paleta(models.Model):
    marca = models.CharField(max_length=30)
    descripcion = RichTextField()
    anio = models.IntegerField()
    
    def __str__(self):
        return f'{self.id} - {self.marca} - {self.anio}'