from django.http import HttpResponse
from datetime import datetime
from django.template import loader


def saludo(request):
    return HttpResponse("hola coders")

def diahoy(request):
    dia = datetime.now()
    documento = f"hoy es {dia} "
    return HttpResponse(documento)

def minombre(request, nombre):
    documento = f"Mi nombre es {nombre} "
    return HttpResponse(documento)

def inicio(request):
    plantilla = loader.get_template("plantillauno.html")
    documento = plantilla.render()

    return HttpResponse(documento)

def vista_template(request):
    listado_alumnos = ["Matias", "Ramiro", "Agustin", "Julian"]
    datos = {"tecnologia": "react", "listado_alumnos": listado_alumnos}


    plantilla = loader.get_template("plantillados.html")
    documento = plantilla.render(datos)

    return HttpResponse(documento)