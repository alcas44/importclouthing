from cgi import print_arguments
from django.shortcuts import render,redirect
from IngresosApp.models import Clientes,Envios
from VentaApp.models import DatosVenta,Detalle
from PagoApp.models import PagoEfectivo
from django.contrib import messages
from django.db.models import Sum
import random
from datetime import date


def pago(request,id,n):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        #datos del cliente
        cliente = Clientes.objects.filter(nit=n)
        #datos de la venta
        datosv = DatosVenta.objects.filter(venta=id)
        #detalle de la venta
        detalle = Detalle.objects.filter(venta=id)
        #nombre del articulos
        t = Detalle.objects.filter(venta=id).aggregate(tot=Sum('total'))
        
        if request.method == "POST":
            if request.POST["tipo"] == "Efectivo":               
                    
                    a = random.sample(range(1000000), 10)
                    p = random.randint(1,10)
                    v = a[-p]
                    e = PagoEfectivo()
                    e.venta = request.POST["venta"]
                    e.nit = request.POST["nit"]
                    e.fecha = request.POST["fecha"]
                    e.total_venta = request.POST["total"]
                    e.tipo_pago = request.POST["tipo"]
                    e.total_pago = request.POST["total"]
                    e.verificador = v
                    e.usuario = request.user.username
                    e.fecha_sistema = date.today()
                    e.save()
                    messages.success(request, 'Pago Efectuado Exitosamente! ¡¡Guarde el Numero de Verificador!!')
                    return redirect('Efectivo',e.verificador,e.nit) 
                     

            elif request.POST["tipo"] == "Cheque":
                pass
            elif request.POST["tipo"] == "Tarjeta":
                pass
            elif request.POST["tipo"] == "Deposito":
                pass
            elif request.POST["tipo"] == "Dolares":
                pass  
        else:
            pass
             #messages.error(request, 'Error al Almacenar Forma de Pago!')
             #return redirect('IniciarVenta')
            

    return render(request,"PagoApp/pago.html",{'v':cliente,'n':datosv,'d':detalle,'t':t})




def efectivo(request,v,n):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        return render(request,"PagoApp/efectivo.html",{'v':v,'n':n})



def envios(request,v,n):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        #print(e.venta,e.nit,e.fecha,e.total_venta,e.tipo_pago,e.total_pago,e.verificador,e.usuario,e.fecha_sistema)

        #datos del cliente
        cliente = Clientes.objects.filter(nit=n)
        #datos del pago en efectivo
        efectivo = PagoEfectivo.objects.filter(nit=n,verificador=v)

        if request.method == "POST":
            e = Envios()
            e.verificador = request.POST["verificador"]
            e.remitente = request.POST["remitente"]
            e.direccion_remitente = request.POST["dir_remitente"]
            e.telefono_remitente = request.POST["tel_remitente"]
            e.destinatario = request.POST["destinatario"]
            e.nit = request.POST["nit"]
            e.direccion =  request.POST["direccion"]
            e.telefono = request.POST["tel"]
            e.venta = request.POST["venta"]
            e.monto = request.POST["totalv"]
            e.total = request.POST["totalp"]
            e.tipo = request.POST["tipo"]
            e.observacion = request.POST["obs"]
            e.estado = 1
            e.usuario = request.user.username
            e.created = date.today()
            e.updated = date.today()
            e.save()
            messages.success(request, 'Ingreso de Envio Exitoso!')
            return redirect('IniciarVenta') 
        


    return render(request,"PagoApp/envio.html",{'v':v,'c':cliente,'e':efectivo})






