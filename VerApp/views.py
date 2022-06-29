import imp
from django.shortcuts import render,redirect
from IngresosApp.models import Articulos

def verarticulo(request,id):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        articulos = Articulos.objects.filter(codigo=id)
        return render(request,"VerApp/articulos.html",{'form':articulos})
