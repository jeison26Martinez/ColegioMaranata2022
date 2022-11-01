from django.shortcuts import render, redirect

def inicioAdmin(request):
    context={}
    return render(request,'index-admin.html', context)

def inicio(request):
    context={}
    return render(request,'index.html', context)

