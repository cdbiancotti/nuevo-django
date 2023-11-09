from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from automovil.models import Automovil
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class ListadoAutomoviles(ListView):
    model = Automovil
    context_object_name = 'listado_de_automoviles'
    template_name = 'automovil/automoviles.html'
    
    def get_queryset(self):
        marca = self.request.GET.get('marca', '')
        if marca:
            listado_de_automoviles = self.model.objects.filter(marca__icontains=marca)
        else:
            listado_de_automoviles = self.model.objects.all()
        return listado_de_automoviles

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["formulario"] = BusquedaAuto()
    #     return context
    
    
class CrearAutomovil(LoginRequiredMixin, CreateView):
    model = Automovil
    template_name = "automovil/crear_automovil.html"
    fields = ['marca', 'modelo', 'descripcion', 'fecha_creacion']
    success_url = reverse_lazy('automoviles')


class ActualizarAutomovil(LoginRequiredMixin, UpdateView):
    model = Automovil
    template_name = "automovil/actualizar_automovil.html"
    fields = ['marca', 'modelo', 'descripcion', 'fecha_creacion']
    success_url = reverse_lazy('automoviles')


class DetalleAutomovil(DetailView):
    model = Automovil
    template_name = "automovil/detalle_automovil.html"


class EliminarAutomovil(LoginRequiredMixin, DeleteView):
    model = Automovil
    template_name = "automovil/eliminar_automovil.html"
    success_url = reverse_lazy('automoviles')
