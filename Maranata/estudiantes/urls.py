from django.urls import path
from estudiantes.views import estudiantes,grado,usuario_listar,usuario_buscar,usuario_modificar


urlpatterns = [
    path('',estudiantes,name="estudiantes"),
    path('grado/',grado,name="grado"),
    path('usuarios/',usuario_listar,name="usuarios-listar"),
    path('usuarios/buscar',usuario_buscar,name="usuarios-buscar"),
    path('usuarios/modificar',usuario_modificar,name="usuarios-modificar"),
]