from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import loader
from inicio.models import Paleta

def inicio(request):
    
    # v2
    # template = loader.get_template('inicio.html')
    # template_renderizado = template.render({})
    
    # return HttpResponse(template_renderizado)
    
    # v3
    return render(request, 'inicio/inicio.html', {})

def paletas(request):
    
    paleta = Paleta(marca='wilson', descripcion='paleta de bela', anio=2022)
    paleta.save()
    
    return render(request, 'inicio/paletas.html', {'paleta': paleta})