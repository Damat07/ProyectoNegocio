from django.shortcuts import render
from Maquinas.models import Maquina
# Create your views here.

def maquinas(request):
    maquinas = Maquina.objects.all()
    if request.method == 'POST':
        nuevaMaquina = Maquina(marca = request.POST['marca'],modelo = request.POST['modelo'],año = request.POST['año'],descripcion = request.POST['descripcion'])
        nuevaMaquina.save()
    return render(request, 'maquinas.html',{'lista_maquinas':maquinas})