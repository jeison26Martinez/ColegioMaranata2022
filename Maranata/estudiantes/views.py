from django.shortcuts import render
from estudiantes.forms import EstudianteForms
# Create your views here.
def estudiantes(request):
    form=EstudianteForms()
    context={
    "form":form 
    }
    return render(request,'estudiantes/estudiantes.html',context)
