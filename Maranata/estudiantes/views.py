from django.shortcuts import render

# Create your views here.
def estudiantes(request):
    context={

    }
    return render(request,'estudiantes/estudiantes.html',context)
