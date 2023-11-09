from django import forms
from inicio.models import Paleta
from ckeditor.fields import RichTextFormField


# otrea version de formulario de paleta
# class PaletaFormulario(forms.Form):
#     class Meta:
#         model = Paleta
#         fields = ['marca', 'descripcion', 'anio']
        

class BasePaletaFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    descripcion = RichTextFormField()
    anio = forms.IntegerField()
    

class CrearPaletaFormulario(BasePaletaFormulario):
    ...


class ActualizarPaletaFormulario(BasePaletaFormulario):
    ...
    
class BusquedaPaletaFormulario(forms.Form):
    marca = forms.CharField(max_length=30, required=False)
    