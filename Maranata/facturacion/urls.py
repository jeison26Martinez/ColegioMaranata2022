from django.urls import path
from facturacion.views import reciboMatricula

urlpatterns = [
    path('reciboMatricula/',reciboMatricula,name="reciboMatricula"),
]