from django.urls import path
from inicio.views import inicio, paletas

urlpatterns = [
    path('', inicio, name='inicio'),
    path('paletas/', paletas, name='paletas'),
]
