from django.shortcuts import render
from estudiantes.forms import EstudianteForms, GradoForms
from estudiantes.models import Usuario
from estudiantes.models import Estudiante
from estudiantes.models import Grado


# Create your views here.
def estudiantes(request):
    form=EstudianteForms()
    context={
    "form":form 
    }
    return render(request,'estudiantes/estudiantes.html',context)


def grado(request):
    form=GradoForms()
    context={
    "form":form
    }
    return render(request,'estudiantes/grado.html',context)


def usuario_listar(request):
    usuarios=Usuario.objects.all()
    context={
        "usuarios":usuarios

    }
    return render(request,"estudiantes/usuarios_listar.html",context)


def usuario_buscar(request):
    usuarios=Usuario.objects.all()
    context={
        "usuarios":usuarios
    }
    return render(request,"estudiantes/usuarios_buscar.html",context)


def usuario_modificar(request):
    usuarios=Usuario.objects.all()
    context={
        "usuarios":usuarios
    }
    return render(request,"estudiantes/usuarios_modificar.html",context)


def estudiante_buscar(request):
    estudiantes=Estudiante.objects.all()
    context={
        "estudiantes":estudiantes
    }
    return render(request,"estudiantes/estudiante_buscar.html",context)


def estudiante_modificar(request):
    estudiantes=Estudiante.objects.all()
    context={
        "estudiante":estudiantes
    }
    return render(request,"estudiantes/estudiante_modificar.html",context)


def estudiante_listar(request):
    estudiantes=Estudiante.objects.all()
    context={
        "estudiante":estudiantes
    }
    return render(request,"estudiantes/estudiante_listar.html",context)


def grado_buscar(request):
    estudiantes=Estudiante.objects.all()
    context={
        "estudiantes":estudiantes
    }
    return render(request,"estudiantes/grado_buscar.html",context)


def grado_modificar(request):
    estudiantes=Estudiante.objects.all()
    context={
        "estudiante":estudiantes
    }
    return render(request,"estudiantes/grado_modificar.html",context)


def grado_listar(request):
    estudiantes=Estudiante.objects.all()
    context={
        "estudiante":estudiantes
    }
    return render(request,"estudiantes/grado_listar.html",context)





    


    
