from django.forms import ModelForm
from estudiantes.models import Estudiante, Grado

class EstudianteForms(ModelForm):
    class Meta: 
        model=Estudiante
        exclude=["estado"]

class GradoForms(ModelForm):
    class Meta:
        model=Grado
        exclude=["estado"]


