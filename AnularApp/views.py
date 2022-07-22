from datetime import date
from django.shortcuts import render,redirect
from IngresosApp.models import Clientes,Articulos
from VentaApp.models import DatosVenta,Detalle
from AnularApp.models import DatosAnulacion,DetalleAnulacion
from django.db.models import Sum
from django.contrib import messages

def anularventa(request):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        
        #obtenemos todas las ventas
        venta = DatosVenta.objects.all().filter(estado=1).select_related("nit")
        
     

        return render(request,"AnularApp/listaventas.html",{'v':venta})




def anularconfirma(request,v,id):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        
       #datos del cliente
        cliente = Clientes.objects.filter(nit=id)
        #datos de la venta
        datosv = DatosVenta.objects.filter(venta=v).filter(estado=1)
        #detalle de la venta
        detalle = Detalle.objects.filter(venta=v)
        #total del detalle
        t = Detalle.objects.filter(venta=v).aggregate(tot=Sum('total'))
        #buscar y actualizar
        cambiodatos = DatosVenta.objects.filter(venta=v)
        cambiodetalle = Detalle.objects.filter(venta=v)
       
        
        
        if request.method == "POST":
            d = DatosAnulacion()
            d.venta = request.POST["venta"]
            d.nit = id
            d.cliente = request.POST["cliente"]
            d.total_venta = request.POST["total"]
            d.motivo = request.POST["motivo"]
            d.fecha_anulacion = date.today()
            d.usuario = request.user.username
            d.fecha_sistema = date.today()
            DatosVenta.objects.filter(venta=request.POST["venta"]).update(estado=2)
            d.save()
           
            dt = DetalleAnulacion()
            dt.venta = DatosAnulacion.objects.get(venta = request.POST["vent"])
            dt.nit = id
            dt.codigo = request.POST["cd"]
            dt.precio = request.POST["pr"]
            dt.cantidad = request.POST["cn"]
            dt.total = request.POST["tt"]
            dt.estado = 1
            dt.fecha_anulacion = date.today()
            dt.usuario = request.user.username
            dt.fecha_sistema = date.today()
            #art = Articulos.objects.filter(codigo=request.POST["cd"])
            #for a in art:
                #nueva_stock = a.existencia
                #Articulos.objects.filter(codigo=request.POST["cd"]).update(existencia=nueva_stock+request.POST["cn"])
            #Articulos.objects.filter(codigo=request.POST["cd"]).update(existencia=request.POST["cn"])
            dt.save()
            messages.success(request, 'Anulacion Exitosa!.')
            return redirect('AnularVenta')
            
        
     

    return render(request,"AnularApp/confirmar.html",{'v':cliente,'n':datosv,'d':detalle,'t':t,'vt':v})

