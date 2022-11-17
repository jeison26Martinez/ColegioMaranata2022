from django.forms import ModelForm
from facturacion.models import ReciboMatricula,AñoLectivo

class ReciboMatriculaForms(ModelForm):
    class Meta:
        model=ReciboMatricula
        fields="__all__"


class AñoLectivoForms(ModelForm):
    class Meta:
        model=AñoLectivo 
        fields="__all__"