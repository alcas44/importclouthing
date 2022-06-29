from django.shortcuts import render,redirect
from IngresosApp.models import Articulos,Clientes


def actualizararti(request,id):
   if not request.user.is_authenticated and not request.user.is_active:
        redirect('/')
   else:
        updatearti = Articulos.objects.filter(codigo=id)
        #agregar el historial de ventas para mostar otros detalles
        return render(request,"ActualizarApp/actualizararti.html",{'form':updatearti})


def verarti(request,id):
   if not request.user.is_authenticated and not request.user.is_active:
        redirect('/')
   else:
        verarti = Articulos.objects.filter(codigo=id)
        #agregar el historial de ventas para mostar otros detalles
        return render(request,"VerArticulos/verarti.html",{'form':verarti})        



def actualizarcliente(request,id):
   if not request.user.is_authenticated and not request.user.is_active:
        redirect('/')
   else:
        updatecli = Clientes.objects.filter(nit=id)
        #agregar el historial de ventas para mostar otros detalles
        return render(request,"ActualizarApp/actualizarcliente.html",{'form':updatecli})
