from _json import make_encoder

from django.forms import modelform_factory
from django.shortcuts import render

from clientes.models import Cliente

ClienteForm = modelform_factory(Cliente, exclude=[])

# Create your views here.
def add_client(request):
    mensaje = ''
    if request.method == 'POST':
        try:
            '''
            nombre = request.POST["nombre"]
            apellidos = request.POST["apellidos"]
            dni = request.POST["dni"]
            email = request.POST["email"]
            print(f'{nombre} {apellidos} {dni} {email}')
            cliente = Cliente(nombre=nombre, apellidos=apellidos, email=email, dni=dni)
            '''
            cliente_form = ClienteForm(request.POST)
            cliente_form.save()
        except Exception as e:
            mensaje = f'Error al almacenar el cliente {e}'
        else:
            mensaje = "Cliente almacenado correctamente"

    cliente_form = ClienteForm()

    contexto = {"cliente_form": cliente_form, "mensaje": mensaje}
    return render(request, "add_client.html", contexto)
