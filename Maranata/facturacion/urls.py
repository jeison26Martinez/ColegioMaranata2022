from django.urls import path
from facturacion.views import reciboMatricula,AñoLectivo,ReciboPension,pazySalvo

urlpatterns = [
    path('reciboMatricula/',reciboMatricula,name="reciboMatricula"),
    path('AñoLectivo/',AñoLectivo,name="AñoLectivo"),
    path('ReciboPension/',ReciboPension,name="ReciboPension"),
    path('pazySalvo/',pazySalvo,name="pazySalvo")
]   