from cgi import print_arguments
from decimal import Decimal
from django.shortcuts import render,redirect
from IngresosApp.models import Clientes,Envios,EnviosCheque
from VentaApp.models import DatosVenta,Detalle
from PagoApp.models import PagoCheque, PagoEfectivo
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
            #viene de Pago
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

            #pago cheque
            elif request.POST["tipo"] == "Cheque":
                a = random.sample(range(1000000), 10)
                p = random.randint(1,10)
                v = a[-p]
                venta = request.POST["venta"]
                n = request.POST["nit"]
                p = request.POST["total"]
                tp = request.POST["tipo"]
                return redirect('Cheque',v,venta,n,p,tp)
            #fin pago cheque

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



def cheque(request,v,vn,n,t,tp):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
         if request.method == "POST":
            pc = PagoCheque()
            pc.venta = vn
            pc.nit = n
            pc.fecha = date.today()
            pc.numero_cheque = request.POST["numero"]
            pc.banco = request.POST["banco"]
            pc.fecha_cheque = request.POST["fechacheque"]
            pc.total_venta = request.POST["total"]
            pc.tipo_pago = request.POST["tipo"]
            pc.abono = request.POST["abono"]
            pc.monto = Decimal(request.POST["total"])-Decimal(request.POST["abono"])    
            pc.verificador = v
            pc.estado = 1
            pc.usuario = request.user.username
            pc.fecha_sistema = date.today()
            pc.save()
            messages.success(request, 'Pago con Cheque Ingresado Exitosamente! ¡¡Guarde el Numero de Verificador y Numero Venta!!')
            return redirect('ChequeOk',v,vn,n)

    return render(request,"PagoApp/cheque.html",{'v':v,'vn':vn,'n':n,'t':t,'tp':tp})



def chequeok(request,v,vn,n):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        return render(request,"PagoApp/chequeok.html",{'v':v,'n':n,'vn':vn})




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





def envioscheque(request,v,n):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        #print(e.venta,e.nit,e.fecha,e.total_venta,e.tipo_pago,e.total_pago,e.verificador,e.usuario,e.fecha_sistema)

        #datos del cliente
        cliente = Clientes.objects.filter(nit=n)
        #datos del pago en efectivo
        cheque = PagoCheque.objects.filter(nit=n,verificador=v)
        for c in cheque:
            r = c.monto-c.abono
            print(r)

        if request.method == "POST":
            e = EnviosCheque()
            e.verificador = request.POST["verificador"]
            e.remitente = request.POST["remitente"]
            e.direccion_remitente = request.POST["dir_remitente"]
            e.telefono_remitente = request.POST["tel_remitente"]
            e.destinatario = request.POST["destinatario"]
            e.nit = request.POST["nit"]
            e.direccion =  request.POST["direccion"]
            e.telefono = request.POST["tel"]
            e.venta = request.POST["venta"]
            e.tipo = request.POST["tipo"]
            e.numero_cheque = request.POST["numerocheque"]
            e.banco = request.POST["banco"]
            e.fecha_cheque = request.POST["fechacheque"]
            e.total = request.POST["totalcheque"]
            e.abono = request.POST["abono"]
            e.restante = Decimal(request.POST["totalcheque"])-Decimal(request.POST["abono"])
            e.observacion = request.POST["obs"]
            e.estado = 1
            e.usuario = request.user.username
            e.created = date.today()
            e.updated = date.today()
            e.save()
            messages.success(request, 'Ingreso de Envio Exitoso!')
            return redirect('IniciarVenta') 
        


    return render(request,"PagoApp/enviocheque.html",{'v':v,'cl':cliente,'c':cheque,'r':r})




