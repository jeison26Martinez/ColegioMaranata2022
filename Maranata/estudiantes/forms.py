from django.forms import ModelForm
from estudiantes.models import Estudiante

class EstudianteForms(ModelForm):
    class Meta: 
        model=Estudiante
        exclude=["estado"]