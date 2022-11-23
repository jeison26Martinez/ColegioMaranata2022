from django.shortcuts import render
from facturacion.forms import ReciboMatriculaForms,AñoLectivoForms,ReciboPensionForms,PazySalvoForms
from facturacion.models import PazySalvo
# Create your views here.
def reciboMatricula(request):
    form=ReciboMatriculaForms()
    context={
    'form':form
    }
    return render(request,'facturacion/reciboMatricula.html',context)


def añoLectivo(request):
    form=AñoLectivoForms()
    context={
    'form':form
    }
    return render(request,'facturacion/AñoLectivo.html',context)


def reciboPension(request):
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

def pazySalvo_listar(request):
    pazySalvos=PazySalvo.objects.all()
    context={
    'pazySalvos':pazySalvos,
    }
    return render(request,'facturacion/pazySalvo_listar.html',context)


