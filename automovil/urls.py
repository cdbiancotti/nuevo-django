from django.urls import path
from automovil.views import ListadoAutomoviles, CrearAutomovil, ActualizarAutomovil, EliminarAutomovil, DetalleAutomovil

urlpatterns = [
    path('automoviles/', ListadoAutomoviles.as_view(), name='automoviles'),
    path('automoviles/crear/', CrearAutomovil.as_view(), name='crear_automovil'),
    path('automoviles/<int:pk>/', DetalleAutomovil.as_view(), name='detalle_automovil'),
    path('automoviles/<int:pk>/actualizar/', ActualizarAutomovil.as_view(), name='actualizar_automovil'),
    path('automoviles/<int:pk>/eliminar/', EliminarAutomovil.as_view(), name='eliminar_automovil'),
]
