from django.db import models

# Create your models here.

class Empleado(models.Model):
    ESTADO_CHOICES = [
        ('activo', 'Activo'),
        ('suspendido', 'Suspendido'),
        ('baja', 'Baja'),
    ]

    empresa_id = models.IntegerField()
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    documento = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    direccion = models.TextField()
    fecha_nacimiento = models.DateField()
    fecha_ingreso = models.DateField()
    unidad_id = models.IntegerField()
    puesto_id = models.IntegerField()
    manager_id = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    foto_url = models.URLField(blank=True, null=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='activo')

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
