from django.shortcuts import render
from estudiantes.forms import EstudianteForms, GradoForms


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







    


    
