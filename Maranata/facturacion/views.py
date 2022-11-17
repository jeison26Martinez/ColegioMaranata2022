from django.shortcuts import render
from facturacion.forms import ReciboMatriculaForms,AñoLectivoForms,ReciboPensionForms,PazySalvoForms

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


def ReciboPension(request):
    form=ReciboPensionForms()
    context={
    'form':form
    }
    return render(request,'facturacion/ReciboPension.html',context)


def pazySalvo(request):
    form=PazySalvoForms()
    context={
    'form':form
    }
    return render(request,'facturacion/pazySalvo.html',context)
