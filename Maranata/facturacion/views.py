from django.shortcuts import render
from facturacion.forms import ReciboMatriculaForms

# Create your views here.
def reciboMatricula(request):
    form=ReciboMatriculaForms()
    context={
    'form':form
    }
    return render(request,'facturacion/reciboMatricula.html',context)
