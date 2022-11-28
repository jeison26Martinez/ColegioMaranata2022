from django.urls import path
from estudiantes.views import estudiantes,grado,usuario_listar,usuario_buscar,usuario_modificar,estudiante_buscar
from estudiantes.views import estudiante_modificar,estudiante_listar,grado_buscar,grado_modificar,grado_listar

urlpatterns = [
    path('',estudiantes,name="estudiantes"),
    path('grado/',grado,name="grado"),
    path('usuarios/',usuario_listar,name="usuarios-listar"),
    path('usuarios/buscar',usuario_buscar,name="usuarios-buscar"),
    path('usuarios/modificar',usuario_modificar,name="usuarios-modificar"),
    path('estudiantes/buscar',estudiante_buscar,name="estudiante-buscar"),
    path('estudiante/modificar',estudiante_modificar,name="estudiante-modificar"),
    path('estudiante/listar',estudiante_listar,name="estudiante-listar"),
    path('grado/buscar',grado_buscar,name="grado-buscar"),
    path('grado/modificar',grado_modificar,name="grado-modificar"),
    path('grado/listar',grado_listar,name="grado-listar"),
]