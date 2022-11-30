from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
'''
def bienvenido(request):
    return HttpResponse("Hola mundo!")


def bienvenido(request):
    return render(request, "bienvenido.html")
'''


def bienvenido(request):
    mensajes = {"mensaje1": "Valor del mensaje1", "mensaje2": "Valor2"}
    return render(request, "bienvenido.html", mensajes)


def listar_alumnos(request):
    listado_alumnos = [
        {"nombre": "Nombre1", "apellidos": "Apellidos1", "dni": "1111A"},
        {"nombre": "Nombre2", "apellidos": "Apellidos2", "dni": "2222B"},
        {"nombre": "Nombre3", "apellidos": "Apellidos3", "dni": "3333C"},
    ]
    contexto = {"listado_alumnos": listado_alumnos}
    return render(request, "gestion/alumnos.html", contexto)

def despedida(request):
    return render(request, "despedida.html")
