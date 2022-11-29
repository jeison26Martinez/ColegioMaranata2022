from django.shortcuts import render, redirect

def login(request):
    context={}
    return render(request,'login.html', context)

def inicioAdmin(request):
    context={}
    return render(request,'index-admin.html', context)

def inicio(request):
    context={}
    return render(request,'index.html', context)

