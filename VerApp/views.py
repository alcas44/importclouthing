import imp
from django.shortcuts import render,redirect
from IngresosApp.models import Articulos,Clientes
from VentaApp.models import Detalle,DatosVenta
from django.db.models import Sum

from VentaApp.views import venta

def verarticulo(request,id):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        articulos = Articulos.objects.filter(codigo=id)
        return render(request,"VerApp/articulos.html",{'form':articulos})



def vercliente(request,id):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        clientes = Clientes.objects.filter(nit=id)
        return render(request,"VerApp/clientes.html",{'form':clientes})        
