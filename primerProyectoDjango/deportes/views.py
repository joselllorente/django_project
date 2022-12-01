from django.shortcuts import render, get_object_or_404


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

    #Miro si tengo datos en la sesion
    listado_seleccion = request.session.get("listado_selecciones", None)

    #Si en la sesion no hay nada
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
            #Creo diccionario con los datos que mandan
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
