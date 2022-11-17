from django.http import HttpResponse
from appcode.models import*
from appcode.forms import*
from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request,"appcode/index.html")

def creacion_curso(request):

    if request.method == "POST":
        nombre_curso = request.POST["curso"]
        numero_camada = request.POST["camada"]
        
        curso= Curso(nombre=nombre_curso, camada=numero_camada)
        curso.save()

    return render(request, "appcode/curso_formulario.html")

def registro_profesores(request):
    if request.method =="POST":

        #validamos que el formulario no tenga problemas
        formulario=ProfesorFormulario(request.POST)
        if formulario.is_valid():
            #recuperamos los datos del atributo del cleaned data
            data = formulario.cleaned_data

            profesor = Profesor(nombre = data["nombre"], apellido = data["apellido"], email=data["email"], profesion=data["profesion"])
            
            profesor.save()


    formulario=ProfesorFormulario()
    contexto={"formulario": formulario}
    return render(request,"appcode/profesores_formularios.html", contexto)

def cursos(request):
    return render(request,"appcode/cursos.html")

def estudiantes(request):
    return render(request,"appcode/estudiantes.html")

def profesores(request):
    return render(request,"appcode/profesores.html")

def entregables(request):
    return render(request,"appcode/entregables.html")

def buscar_curso(request):

    return render(request, "appcode/busqueda_cursos.html")

def resultados_busqueda_cursos(request):
    nombre_curso = request.GET["nombre_curso"]

    cursos = Curso.objects.filter(nombre__icontains=nombre_curso)
    return render(request, "appcode/resultados_busquedas_cursos.html", {"cursos": cursos})
