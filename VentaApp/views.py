from calendar import c
from tkinter import EW
from django.shortcuts import render,redirect
from IngresosApp.models import Articulos,Clientes
from VentaApp.models import DatosVenta, Detalle
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
            return redirect('Venta',v.venta,v.nit)    
        else:
            contador = contador + 1
            return render(request,"VentaApp/iniciar.html",{'c':contador})    

    return render(request,"VentaApp/iniciar.html",{'c':contador})
    


acu = 0.00

def venta(request,id,n):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        art = Articulos.objects.all().order_by()
        cliente = Clientes.objects.filter(nit=n)
        if request.method == "POST":
            global acu
            if "fin" in request.POST:
                return redirect("FinVenta",id,n)
            else:
                stock = Articulos.objects.filter(codigo=request.POST["codigo"])
                for s in stock:
                    if s.existencia <= int(request.POST["cantidad"]):
                        messages.error(request, 'Cantidad NO Puede Ser Mayor a la Existencia!.')
                        return redirect('Venta',id,n)
                    else:
                        d = Detalle()  
                        acu = acu +float(request.POST["precio"])*int(request.POST["cantidad"])
                        d.venta = id
                        d.codigo = request.POST["codigo"]
                        d.precio = request.POST["precio"]
                        d.cantidad = request.POST["cantidad"]
                        d.total = float(request.POST["precio"])*int(request.POST["cantidad"])
                        d.estado = 0
                        d.save()
                        messages.error(request, 'Articulo Agregado Exitosamente!.')  
                    
        else:
            pass    
          
    return render(request,"VentaApp/venta.html",{'art':art,'cli':cliente,'acu':acu})



def fin_venta(request,id,n):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        cliente = Clientes.objects.filter(nit=n)
        resumen = Detalle.objects.filter(venta=id)
        if request.method == "POST":
            DatosVenta.objects.filter(venta=id).update(estado=1)
            for r in resumen:
                Detalle.objects.filter(venta=id,codigo=r.codigo).update(estado=1)   
                art = Articulos.objects.filter(codigo=r.codigo)
                for a in art:
                    nueva_stock = a.existencia-r.cantidad
                    Articulos.objects.filter(codigo=r.codigo).update(existencia=nueva_stock)                            
            messages.success(request, 'Venta Finaliza Exitosamente!.')
            return redirect('IniciarVenta')
        else:
            pass    
          
    return render(request,"VentaApp/finalizar.html",{'cli':cliente,'resumen':resumen})





