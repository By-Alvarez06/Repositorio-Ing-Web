from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import JsonResponse
from .models import Empleado

# Create your views here.

class EmpleadoListView(ListView):
    model = Empleado
    template_name = 'empleados/empleado_list.html'
    context_object_name = 'empleados'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        empleados = context['empleados']
        context['total_empleados'] = empleados.count()
        context['activos'] = empleados.filter(estado='activo').count()
        context['inactivos'] = empleados.filter(estado__in=['suspendido', 'baja']).count()
        return context

def empleado_json(request, pk):
    try:
        empleado = Empleado.objects.get(pk=pk)
        data = {
            'empresa_id': empleado.empresa_id,
            'nombres': empleado.nombres,
            'apellidos': empleado.apellidos,
            'documento': empleado.documento,
            'email': empleado.email,
            'telefono': empleado.telefono,
            'direccion': empleado.direccion,
            'fecha_nacimiento': str(empleado.fecha_nacimiento),
            'fecha_ingreso': str(empleado.fecha_ingreso),
            'unidad_id': empleado.unidad_id,
            'puesto_id': empleado.puesto_id,
            'manager_id': empleado.manager_id.id if empleado.manager_id else '',
            'foto_url': empleado.foto_url,
            'estado': empleado.estado,
        }
        return JsonResponse(data)
    except Empleado.DoesNotExist:
        return JsonResponse({'error': 'Empleado no encontrado'}, status=404)

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
