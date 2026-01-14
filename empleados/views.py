from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Empleado

# Create your views here.

class EmpleadoListView(ListView):
    model = Empleado
    template_name = 'empleados/empleado_list.html'
    context_object_name = 'empleados'

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'empleados/empleado_detail.html'

class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = 'empleados/empleado_form.html'
    fields = ['empresa_id', 'nombres', 'apellidos', 'documento', 'email', 'telefono', 'direccion', 'fecha_nacimiento', 'fecha_ingreso', 'unidad_id', 'puesto_id', 'manager_id', 'foto_url', 'estado']
    success_url = reverse_lazy('empleado_list')

class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = 'empleados/empleado_form.html'
    fields = ['empresa_id', 'nombres', 'apellidos', 'documento', 'email', 'telefono', 'direccion', 'fecha_nacimiento', 'fecha_ingreso', 'unidad_id', 'puesto_id', 'manager_id', 'foto_url', 'estado']
    success_url = reverse_lazy('empleado_list')

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'empleados/empleado_confirm_delete.html'
    success_url = reverse_lazy('empleado_list')
