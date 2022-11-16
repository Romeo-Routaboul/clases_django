from django.urls import path
from appcode.views import*

urlpatterns = [
    path("inicio/", inicio, name='coder-inicio'),
    path("estudiantes/", estudiantes, name='coder-estudiantes'),
    path("entregables/",entregables, name='coder-entregables' ),
    path("cursos/", cursos, name='coder-cursos'),
    path("profesores/", profesores, name='coder-profesores'),




]