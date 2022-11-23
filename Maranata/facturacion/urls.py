from django.urls import path
from facturacion.views import reciboMatricula,añoLectivo,reciboPension,pazySalvo,pazySalvo_listar

urlpatterns = [
    path('reciboMatricula/',reciboMatricula,name="reciboMatricula"),
    path('anioLectivo/',añoLectivo,name="añoLectivo"),
    path('reciboPension/',reciboPension,name="reciboPension"),
    path('pazySalvo/',pazySalvo,name="pazySalvo"),
    path('pazySalvo/listar',pazySalvo_listar,name="pazySalvo-listar"),

]   