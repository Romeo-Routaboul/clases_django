from django.urls import path
from appcode.views import*

urlpatterns = [
    path("inicio/", inicio),
    path("estudiantes/", estudiantes),
    path("entregable/",entregables ),
    path("curso/", cursos),
    path("profesores/", profesores),




]