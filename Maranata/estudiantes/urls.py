from django.urls import path
from estudiantes.views import estudiantes,grado


urlpatterns = [
    path('',estudiantes,name="estudiantes"),
    path('grado/',grado,name="grado"),
    
]