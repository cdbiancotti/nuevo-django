from django.urls import path
from inicio.views import inicio, paletas, crear_paleta, eliminar_paleta, actualizar_paleta, detalle_paleta

urlpatterns = [
    path('', inicio, name='inicio'),
    path('paletas/', paletas, name='paletas'),
    path('paletas/crear/', crear_paleta, name='crear_paleta'),
    path('paletas/<int:paleta_id>/', detalle_paleta, name='detalle_paleta'),
    path('paletas/<int:paleta_id>/eliminar/', eliminar_paleta, name='eliminar_paleta'),
    path('paletas/<int:paleta_id>/actualizar/', actualizar_paleta, name='actualizar_paleta'),
]
