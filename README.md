# Repositorio-Ing-Web

Proyecto Django para gestión de empleados con operaciones CRUD.

## Configuración del Entorno

1. Activar el entorno virtual:
   ```
   .\venv\Scripts\activate
   ```

2. Instalar dependencias:
   ```
   pip install -r requirements.txt
   ```

3. Aplicar migraciones:
   ```
   python manage.py migrate
   ```

4. Ejecutar el servidor:
   ```
   python manage.py runserver
   ```

## URLs Disponibles

- `/empleados/`: Lista de empleados
- `/empleados/create/`: Crear nuevo empleado
- `/empleados/<id>/`: Detalle de empleado
- `/empleados/<id>/update/`: Editar empleado
- `/empleados/<id>/delete/`: Eliminar empleado

## Modelo Empleado

- nombre: CharField
- apellido: CharField
- email: EmailField (único)
- fecha_contratacion: DateField
- salario: DecimalField
