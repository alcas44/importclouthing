from django.shortcuts import render,redirect
from IngresosApp.models import Articulos, Clientes
from IngresosApp.forms import ClientesForm
from datetime import date, datetime


def historialcliente(request):
    if not request.user.is_authenticated and not request.user.is_active:
        redirect('/')
    else:
        allcliente = Clientes.objects.all()
        return render(request,"HistorialApp/historialcliente.html",{'cliente':allcliente})



def detallecliente(request,id):
   if not request.user.is_authenticated and not request.user.is_active:
        redirect('/')
   else:
        detalles = Clientes.objects.filter(nit=id)
        #agregar el historial de ventas para mostar otros detalles
        return render(request,"HistorialApp/detallecliente.html",{'form':detalles})




def inventarioarticulos(request):
    if not request.user.is_authenticated and not request.user.is_active:
        redirect('/')
    else:
        allarti = Articulos.objects.all()
        return render(request,"HistorialApp/inventarioarticulos.html",{'inventario':allarti})
