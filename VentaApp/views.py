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
            print(request.POST["fin"])
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
            stock = Articulos.objects.filter(existencia__gt=request.POST["cantidad"])#verifica si es stock es >= a cantidad
            if not stock:
                messages.error(request, 'Cantidad NO Puede Ser Mayor a la Existencia!.')
                return redirect('Venta',id)  
            else:
                print("Venta--> "+str(id))
                print("Codigo--> "+request.POST["codigo"])
                print("Precio--> "+request.POST["precio"])
                print("Cantidad--> "+request.POST["cantidad"])
                print("Total--> "+request.POST["total"])
                print("Estado Venta--> "+str(0))
                if 'fin' in request.POST:
                    messages.success(request, 'Resumen de la Venta!.')
                    return redirect('FinVenta',id)
                else:
                    messages.success(request, 'Articulo Agregado a Carrito Exitosamente!.')
                    return redirect('Venta',id)  
            
        else:
            pass    
          
    return render(request,"VentaApp/venta.html",{'art':art})



def fin_venta(request,id):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        datosventa = DatosVenta.objects.filter(venta=id) 
        if request.method == "POST":
            print("Venta--> "+str(id))
            #messages.success(request, 'Venta Finaliza Exitosamente!.')
            #return redirect('InicarVenta')
        else:
            pass    
          
    return render(request,"VentaApp/finalizar.html",{'id':id})





