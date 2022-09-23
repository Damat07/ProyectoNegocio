from django.http import HttpResponse
from django.shortcuts import render
from Clientes.models import Cliente
# Create your views here.

def clientes(request):
    comentarios = Cliente.objects.all()
    if request.method == 'POST':
        nuevoComentario = Cliente(nombre = request.POST['nombre'],comentario = request.POST['comentario'])
        nuevoComentario.save()
    return render(request, 'clientes.html',{'comentarios':comentarios})

def buscar_comentarios(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        lista_comentarios = Cliente.objects.filter(nombre__icontains = nombre)
        return render(request, 'clientes.html', {'lista_comentarios':lista_comentarios})