from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory

from deportes.models import Jugador


# Create your views here.
def deportes(request):
    contenido = {"titulo_pagina": "Actualidad deportiva",
                 "descripcion": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod "
                                "tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, "
                                "quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. "}
    return render(request, "deportes.html", contenido)


def listar_selecciones(request):
    espania = {"nombre": "España", "continente": "Europa", "num_mundiales": 1}
    brasil = {"nombre": "Brasil", "continente": "America", "num_mundiales": 5}
    francia = {"nombre": "Francia", "continente": "Europa", "num_mundiales": 2}
    senegal = {"nombre": "Senegal", "continente": "Africa", "num_mundiales": 0}

    lista_selecciones = [espania, brasil, francia, senegal]

    # Miro si tengo datos en la sesion
    listado_seleccion = request.session.get("listado_selecciones", None)

    # Si en la sesion no hay nada
    if listado_seleccion == None:
        request.session['listado_selecciones'] = lista_selecciones
        listado_seleccion = lista_selecciones

    continente_filtro = None
    if request.method == 'POST':
        titulo = "hola"
        accion = request.POST.get('action', '')

        if accion == "filtrar":
            continente_filtro = request.POST['continente']
            titulo = request.POST.get('titulo', 'Titulo por Defecto')

            listado_seleccion = list(
                filter(lambda seleccion: seleccion["continente"] == continente_filtro, listado_seleccion))

        elif accion == "guardar":
            nombre = request.POST["nombre"]
            continente = request.POST["continente"]
            num_mundiales = request.POST["mundiales"]
            # Creo diccionario con los datos que mandan
            nueva_seleccion = {"nombre": nombre, "continente": continente, "num_mundiales": num_mundiales}
            listado_seleccion.append(nueva_seleccion)

            request.session['listado_selecciones'] = listado_seleccion

            titulo = request.POST.get('titulo', 'Titulo por Defecto')

    elif request.method == 'GET':
        # titulo = request.parameter("titulo")
        # titulo = request.GET['titulo']
        titulo = request.GET.get('titulo', 'Titulo por Defecto')

    contexto = {"listado_selecciones": listado_seleccion, "titulo_tabla": titulo,
                "listado_continentes": ["Europa", "America", "Asia", "Africa", "Oceania"]}

    return render(request, "futbol/listado_selecciones_mundial.html", contexto)


def aniadir_seleccion(request):
    return render(request, "futbol/aniadir_seleccion.html")


def listar_jugadores(request, order=None):
    if request.method == 'POST':
        nacionalidad = request.POST.get('nacionalidad')
        equipo = request.POST.get('equipo')
        posicion = request.POST.get('posicion')

        jugador_objs = Jugador.objects
        if nacionalidad:
            jugador_objs = jugador_objs.filter(nacionalidad=nacionalidad)
        if equipo:
            jugador_objs = jugador_objs.filter(equipo=equipo)
        if posicion:
            jugador_objs = jugador_objs.filter(posicion=posicion)

        if not nacionalidad and not equipo and not posicion:
            jugadores = jugador_objs.all()
        else:
            jugadores = jugador_objs

    else:
        if order:
            print(f"Ordenando por {order}")
            jugadores = Jugador.objects.order_by(order)
        else:
            jugadores = Jugador.objects.all()

    contexto = {"jugadores": jugadores}
    return render(request, "jugadores.html", contexto)


JugadorForm = modelform_factory(Jugador, exclude=[])


def nuevo_jugador(request):
    if request.method == 'POST':

        # Si llega id es una actualizacion
        id = request.POST.get('id')
        if id:
            print(f"Actualizamos jugador con id: {id}")
            jugador = get_object_or_404(Jugador, pk=id)
            jugador_form = JugadorForm(request.POST, instance=jugador)
            jugador_form.save()
        else:
            jugador = JugadorForm(request.POST)
            jugador.save()

        return redirect("jugadores")
    else:
        jugador_form = JugadorForm()

        contexto = {"jugador_form": jugador_form}
        return render(request, "nuevo_jugador.html", contexto)


def delete_jugador(request, id):
    jugador = get_object_or_404(Jugador, pk=id)
    jugador.delete()
    print("Jugador borrado")

    return redirect("jugadores")


def update_jugador(request, id):
    jugador = get_object_or_404(Jugador, pk=id)

    jugador_form = JugadorForm(instance=jugador)

    contexto = {"jugador_form": jugador_form, "id": id}
    return render(request, "nuevo_jugador.html", contexto)
