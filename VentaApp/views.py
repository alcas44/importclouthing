from calendar import c
from tkinter import EW
from django.shortcuts import render,redirect
from IngresosApp.models import Articulos,Clientes
from VentaApp.models import DatosVenta
from datetime import datetime
from django.contrib import messages

contador = 0

def iniciar(request):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        global contador
        if request.method == "POST":
            v = DatosVenta()
            v.venta = request.POST["venta"]
            v.nit = request.POST["nit"]
            v.fecha_venta = request.POST["fecha"]
            v.vendedor = request.POST["usuario"]
            v.estado = 0
            v.save()
            contador = contador + 1
            return redirect('Venta',v.venta)
        else:
            contador = contador + 1
            return render(request,"VentaApp/iniciar.html",{'c':contador})    

    return render(request,"VentaApp/iniciar.html",{'c':contador})
    


def venta(request,id):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        art = Articulos.objects.all().order_by() 
        if request.method == "POST":
            print("Venta--> "+str(id))
            print("Codigo--> "+request.POST["codigo"])
            print("Cantidad--> "+request.POST["cantidad"])
            messages.success(request, 'Articulo Agregado a Carrito Exitosamente!.')
            return redirect('Venta',id)
        else:
            pass    
          
    return render(request,"VentaApp/venta.html",{'art':art})