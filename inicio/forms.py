from django import forms


class BasePaletaFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=250)
    anio = forms.IntegerField()
    

class CrearPaletaFormulario(BasePaletaFormulario):
    ...


class ActualizarPaletaFormulario(BasePaletaFormulario):
    ...
    
class BusquedaPaletaFormulario(forms.Form):
    marca = forms.CharField(max_length=30, required=False)
    