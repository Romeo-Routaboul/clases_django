from django.http import HttpResponse
from appcode.models import Curso
from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request,"appcode/index.html")
def cursos(request):
    return render(request,"appcode/cursos.html")
def estudiantes(request):
    return render(request,"appcode/estudiantes.html")
def profesores(request):
    return render(request,"appcode/profesores.html")
def entregables(request):
    return render(request,"appcode/entregables.html")