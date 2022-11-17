from django.shortcuts import render
from facturacion.forms import ReciboMatriculaForms,AñoLectivoForms

# Create your views here.
def reciboMatricula(request):
    form=ReciboMatriculaForms()
    context={
    'form':form
    }
    return render(request,'facturacion/reciboMatricula.html',context)


def AñoLectivo(request):
    form=AñoLectivoForms()
    context={
    'form':form
    }
    return render(request,'facturacion/AñoLectivo.html',context)
