from django.shortcuts import redirect,render
from facturacion.forms import ReciboMatriculaForms,AñoLectivoForms,ReciboPensionForms,PazySalvoForms
from facturacion.models import AñoLectivo,ReciboPension,PazySalvo
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

def añoLectivo_buscar(request):
    añoLectivo=AñoLectivo.objects.all()
    context={
    'añoLectivo':añoLectivo
    }
    return render(request,'facturacion/añoLectivo_buscar.html',context)

def añoLectivo_modificar(request):
    añoLectivo=AñoLectivo.objects.all()
    context={
    'añoLectivo':añoLectivo
    }
    return render(request,'facturacion/añoLectivo_modificar.html',context)

def añoLectivo_listar(request):
    añoLectivo=AñoLectivo.objects.all()
    context={
    'añoLectivo':añoLectivo
    }
    return render(request,'facturacion/añoLectivo_listar.html',context)


def reciboPension(request):
    form=ReciboPensionForms()
    context={
    'form':form
    }
    return render(request,'facturacion/ReciboPension.html',context)


def reciboPension_buscar(request):
    reciboPensiones=ReciboPension.objects.all()
    context={
    'reciboPensiones':reciboPensiones
    }
    return render(request,'facturacion/reciboPension_buscar.html',context)

def reciboPension_modificar(request):
    reciboPensiones=ReciboPension.objects.all()
    context={
    'reciboPensiones':reciboPensiones
    }
    return render(request,'facturacion/reciboPension_modificar.html',context)

def reciboPension_listar(request):
    reciboPensiones=ReciboPension.objects.all()
    context={
    'reciboPensiones':reciboPensiones
    }
    return render(request,'facturacion/reciboPension_listar.html',context)


def pazySalvo(request):
    if request.method == "POST":
        form=PazySalvoForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pazySalvo')
        else:
            print("Error")
    else:
        form=PazySalvoForms()
    context={
    'form':form
    }
    return render(request,'facturacion/pazySalvo.html',context)

def pazySalvo_buscar(request):
    pazySalvos=PazySalvo.objects.all()
    context={
    'pazySalvos':pazySalvos
    }
    return render(request,'facturacion/pazySalvo_buscar.html',context)

def pazySalvo_modificar(request):
    pazySalvos=PazySalvo.objects.all()
    context={
    'pazySalvos':pazySalvos
    }
    return render(request,'facturacion/pazySalvo_modificar.html',context)

def pazySalvo_listar(request):
    pazySalvos=PazySalvo.objects.all()
    context={
    'pazySalvos':pazySalvos
    }
    return render(request,'facturacion/pazySalvo_listar.html',context)


