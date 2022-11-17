from django.urls import path
from appcode.views import*

urlpatterns = [
    path("inicio/", inicio, name='coder-inicio'),
    path("estudiantes/", estudiantes, name='coder-estudiantes'),
    path("entregables/",entregables, name='coder-entregables' ),
    path("cursos/", cursos, name='coder-cursos'),
    path("cursos/crear/", creacion_curso, name="coder-curso-crear"),
    path("profesores/", profesores, name='coder-profesores'),
    path("profesores/crear/", registro_profesores , name='coder-profesores-crear'),
    path("cursos/buscar/", buscar_curso, name="coder-cursos-buscar"),
    path("cursos/buscar/resultados/", resultados_busqueda_cursos, name="coder-cursos-buscar-resultados"),


]