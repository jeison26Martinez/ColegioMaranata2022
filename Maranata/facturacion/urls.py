from django.urls import path
from facturacion.views import reciboMatricula,AñoLectivo

urlpatterns = [
    path('reciboMatricula/',reciboMatricula,name="reciboMatricula"),
    path('AñoLectivo/',AñoLectivo,name="AñoLectivo")
]