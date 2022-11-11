from django.http import HttpResponse
from appcode.models import Curso

# Create your views here.

def listado_cursos(request):
    cursos = Curso.objects.all()

    cadena_respuesta= ""
    for curso in cursos:
        cadena_respuesta += curso.nombre + " || "
    
    return HttpResponse(cadena_respuesta)