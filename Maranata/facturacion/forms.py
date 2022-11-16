from django.forms import ModelForm
from facturacion.models import ReciboMatricula

class ReciboMatriculaForms(ModelForm):
    class Meta:
        model=ReciboMatricula
        fields="__all__"