from django.shortcuts import render,redirect
from IngresosApp.models import Clientes
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
        detalles = Clientes.objects.filter(id=id)
        #agregar el historial de ventas para mostar otros detalles
        return render(request,"HistorialApp/detallecliente.html",{'form':detalles})
