from django.urls import path
from facturacion.views import reciboMatricula,añoLectivo,añoLectivo_buscar,añoLectivo_modificar,añoLectivo_listar,reciboPension,reciboPension_buscar
from facturacion.views import reciboPension_modificar,reciboPension_listar,pazySalvo,pazySalvo_buscar,pazySalvo_modificar,pazySalvo_listar,reciboMatricula_buscar,reciboMatricula_modificar

urlpatterns = [
    path('reciboMatricula/',reciboMatricula,name="reciboMatricula"),
    path('reciboMatricula/buscar',reciboMatricula_buscar,name="reciboMatricula-buscar"),
    path('reciboMatricula/modificar',reciboMatricula_modificar,name="reciboMatricula-modificar"),
    path('anioLectivo/',añoLectivo,name="añoLectivo"),
    path('anioLectivo/buscar',añoLectivo_buscar,name="añoLectivo-buscar"),
    path('anioLectivo/modificar',añoLectivo_modificar,name="añoLectivo-modificar"),
    path('anioLectivo/listar',añoLectivo_listar,name="añoLectivo-listar"),
    path('reciboPension/',reciboPension,name="reciboPension"),
    path('reciboPension/buscar',reciboPension_buscar,name="reciboPension-buscar"),
    path('reciboPension/modificar',reciboPension_modificar,name="reciboPension-modificar"),
    path('reciboPension/listar',reciboPension_listar,name="reciboPension-listar"),
    path('pazySalvo/',pazySalvo,name="pazySalvo"),
    path('pazySalvo/buscar',pazySalvo_buscar,name="pazySalvo-buscar"),
    path('pazySalvo/modificar',pazySalvo_modificar,name="pazySalvo-modificar"),
    path('pazySalvo/listar',pazySalvo_listar,name="pazySalvo-listar"),
    


]   