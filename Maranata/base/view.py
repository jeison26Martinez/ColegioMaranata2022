from django.shortcuts import render, redirect
from estudiantes.forms import UsuarioForms
from django.contrib import messages




def inicioAdmin(request):
    context={}
    return render(request,'index-admin.html', context)

def inicio(request):
    if request.method=='POST':
        form=UsuarioForms(request.POST)
        print('Hola mundo',form.is_valid(),form)
        if form.is_valid():
            form.save()
            messages.success(
                request,f"Se agregó el usuario {request.POST['nombres']} exitosamente"
            )
            return redirect("/estudiantes/usuarios/")
        else:
            form=UsuarioForms(request.POST)
    else:
        form=UsuarioForms()
    context={
        "form":form
    }
    return render(request,'index.html', context)

