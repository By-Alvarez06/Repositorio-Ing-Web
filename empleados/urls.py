from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmpleadoListView.as_view(), name='empleado_list'),
    path('<int:pk>/', views.EmpleadoDetailView.as_view(), name='empleado_detail'),
    path('create/', views.EmpleadoCreateView.as_view(), name='empleado_create'),
    path('<int:pk>/update/', views.EmpleadoUpdateView.as_view(), name='empleado_update'),
    path('<int:pk>/delete/', views.EmpleadoDeleteView.as_view(), name='empleado_delete'),
    path('<int:pk>/json/', views.empleado_json, name='empleado_json'),
]