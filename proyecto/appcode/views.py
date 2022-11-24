from django.http import HttpResponse
from appcode.models import*
from appcode.forms import*
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Dependencias para resolver apertura de archivos usando rutas relativas
from proyecto.settings import BASE_DIR
import os

# Create your views here.
def inicio(request):
    return render(request,"appcode/index.html")


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
    errores= ""

    # validamos tipo de petición
    if request.method == "POST":
        #cargamos los datos en el formulario
        formulario = CursoFormulario(request.POST)

        # Validamos los datos
        if formulario.is_valid():
            #recuperamos los datos sanitisados
            data = formulario.cleaned_data
            #creamos el curso
            curso = Curso(nombre = data["nombre"], camada=data["camada"])
            #guardamos el curso
            curso.save()
        else:
            #si el formulario no es valido guardamos los errores para mostrarlos
            errores = formulario.errors

    #Recuperar todos los cursos de la BD
    cursos = Curso.objects.all() #obtener todos los registros de ese modelo
    #creamos el formulario vacio
    formulario = CursoFormulario()
    #creamos el contexto
    contexto = {"listado_cursos": cursos, "formulario": formulario, "errores": ""}
    #retornamos la respuesta
    return render(request,"appcode/cursos.html", contexto)

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


def test(request):
    ruta = os.path.join(BASE_DIR, "appcode/templates/appcode/cursos.html")
    print(BASE_DIR, __file__)
    file = open(ruta)

    return HttpResponse(file.read())

def eliminar_curso(request, id):
    curso=Curso.objects.get(id=id)
    curso.delete()

    return redirect("coder-cursos")

def editar_curso(request, id):
    curso = Curso.objects.get(id=id)

    if request.method == "POST":
        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            curso.nombre = data["nombre"]
            curso.camada = data["camada"]
            curso.save()
            return redirect("coder-cursos")
        else:
            return render(request, "appcode/editar_curso.html", {"formulario": formulario, "errores": formulario.errors})    

    else:
        formulario = CursoFormulario(initial={"nombre": curso.nombre, "camada": curso.camada})
        return render(request, "appcode/editar_curso.html", {"formulario": formulario, "errores": ""})
    

class EntregablesList(ListView):

    model = Entregable
    template_name = "appcode/list_entregables.html"


class EntregableDetail(DetailView):

    model = Entregable
    template_name = "appcode/detail_entregable.html"


class EntregableCreate(CreateView):

    model = Entregable
    success_url = "/coder/entregables/"
    fields = ["nombre", "fecha_de_entrega", "entregado"]
    template_name = "appcode/entregable_form.html"

class EntregableUpdate(UpdateView):

    model = Entregable
    success_url = "/coder/entregables/"
    fields = ["fecha_de_entrega", "entregado"]

class EntregableDelete(DeleteView):

    model = Entregable
    success_url = "/coder/entregables/"