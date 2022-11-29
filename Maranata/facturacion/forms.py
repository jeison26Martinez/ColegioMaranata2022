from django.forms import ModelForm
from facturacion.models import ReciboMatricula,AñoLectivo,ReciboPension,PazySalvo

class ReciboMatriculaForms(ModelForm):
    class Meta:
        model=ReciboMatricula
        fields="__all__"


class AñoLectivoForms(ModelForm):
    class Meta:
        model=AñoLectivo 
        fields="__all__"


class ReciboPensionForms(ModelForm):
    class Meta:
        model=ReciboPension
        exclude=["estado"]


class PazySalvoForms(ModelForm):
    class Meta:
        model=PazySalvo
        fields="__all__"
        exclude=["estado"]