from django.shortcuts import render
from estudiantes.forms import EstudianteForms, GradoForms
from estudiantes.models import Usuario


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









    


    
