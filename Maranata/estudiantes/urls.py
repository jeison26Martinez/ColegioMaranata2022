from django.urls import path
from estudiantes.views import estudiantes 

urlpatterns = [
    path('',estudiantes,name="estudiantes"),
]