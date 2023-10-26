from django.urls import path
from inicio.views import inicio, paletas, crear_paleta

urlpatterns = [
    path('', inicio, name='inicio'),
    path('paletas/', paletas, name='paletas'),
    path('paletas/crear/', crear_paleta, name='crear_paleta')
]
