from django.urls import path
from Clientes.vistasClientes import *

urlpatterns = [
    path('', clientes),
    path('buscar_comentarios', buscar_comentarios)
]
