from django.shortcuts import render
from Equipo.models import Empleado
from django.http import HttpResponse

# Create your views here.

def equipo(request):
    integrantes = Empleado.objects.all()
    if request.method == 'POST':
        nuevoEmpleado = Empleado(nombre = request.POST['nombre'],apellido = request.POST['apellido'],edad = request.POST['edad'],puesto = request.POST['puesto'])
        nuevoEmpleado.save()
    return render(request, 'equipo.html',{'lista_empleados':integrantes})