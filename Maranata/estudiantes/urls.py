from django.urls import path
from estudiantes.views import estudiantes,grado,usuario_listar


urlpatterns = [
    path('',estudiantes,name="estudiantes"),
    path('grado/',grado,name="grado"),
    path('usuarios/',usuario_listar,name="usuarios-listar")
    
]