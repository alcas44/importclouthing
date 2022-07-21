from cgi import print_arguments
from decimal import Decimal
from django.shortcuts import render,redirect
from IngresosApp.models import Clientes,Envios,EnviosCheque, EnviosNotaCredito, EnviosTarjeta,EnviosDeposito
from VentaApp.models import DatosVenta,Detalle
from PagoApp.models import NotaCredito, PagoCheque, PagoEfectivo,PagoTarjeta,PagoDeposito
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

            #pago tarjeta
            elif request.POST["tipo"] == "Tarjeta":
                a = random.sample(range(1000000), 10)
                p = random.randint(1,10)
                v = a[-p]
                venta = request.POST["venta"]
                n = request.POST["nit"]
                p = request.POST["total"]
                tp = request.POST["tipo"]
                return redirect('Tarjeta',v,venta,n,p,tp)
            #fin pago tarjeta

            #pago deposito
            elif request.POST["tipo"] == "Deposito":
                a = random.sample(range(1000000), 10)
                p = random.randint(1,10)
                v = a[-p]
                venta = request.POST["venta"]
                n = request.POST["nit"]
                p = request.POST["total"]
                tp = request.POST["tipo"]
                return redirect('Deposito',v,venta,n,p,tp)
            #fin pago deposito

            #pago notacredito
            elif request.POST["tipo"] == "Credito":
                a = random.sample(range(1000000), 10)
                p = random.randint(1,10)
                v = a[-p]
                venta = request.POST["venta"]
                n = request.POST["nit"]
                p = request.POST["total"]
                tp = request.POST["tipo"]
                return redirect('NotaCredito',v,venta,n,p,tp)
            #fin pago notacredito  
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



def tarjeta(request,v,vn,n,t,tp):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
         if request.method == "POST":
            pc = PagoTarjeta()
            pc.venta = vn
            pc.nit = n
            pc.fecha = date.today()
            pc.numero_tarjeta = request.POST["numero"]
            pc.tipo_pago = request.POST["tipo"]
            pc.tipo_tarjeta = request.POST["tipo_tarjeta"]
            pc.banco = request.POST["banco"]
            pc.autorizacion = request.POST["autorizacion"]
            pc.total_venta = request.POST["total"]
            pc.verificador = v
            pc.estado = 1
            pc.usuario = request.user.username
            pc.fecha_sistema = date.today()
            pc.observaciones = request.POST["obs"]
            pc.save()
            messages.success(request, 'Pago con Tarjeta Ingresado Exitosamente! ¡¡Guarde el Numero de Verificador y Numero Venta!!')
            return redirect('TarjetaOk',v,vn,n)

    return render(request,"PagoApp/tarjeta.html",{'v':v,'vn':vn,'n':n,'t':t,'tp':tp})




def deposito(request,v,vn,n,t,tp):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
         if request.method == "POST":
            pc = PagoDeposito()
            pc.venta = vn
            pc.nit = n
            pc.fecha = date.today()
            pc.tipo_pago = request.POST["tipo"]
            pc.numero_boleta = request.POST["numero"]
            pc.banco = request.POST["banco"]
            pc.monto_deposito = request.POST["monto"]
            pc.fecha_deposito = request.POST["fechadepo"]
            pc.total_venta = request.POST["total"] 
            pc.verificador = v
            pc.observaciones = request.POST["obs"]
            pc.estado = 1
            pc.usuario = request.user.username
            pc.fecha_sistema = date.today()
            pc.save()
            messages.success(request, 'Pago con Deposito Ingresado Exitosamente! ¡¡Guarde el Numero de Verificador y Numero Venta!!')
            return redirect('DepositoOk',v,vn,n)

    return render(request,"PagoApp/deposito.html",{'v':v,'vn':vn,'n':n,'t':t,'tp':tp})





def notacredito(request,v,vn,n,t,tp):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
         if request.method == "POST":
            pc = NotaCredito()
            pc.venta = vn
            pc.nit = n
            pc.fecha = date.today()
            pc.tipo_pago = request.POST["tipo"]
            pc.numero_credito = request.POST["nota"]
            pc.fecha_inicio = request.POST["inicio"]
            pc.fecha_fin = request.POST["fin"].strftime("%d-%m-%Y")
            pc.total_venta = request.POST["total"] 
            pc.verificador = v
            pc.observaciones = request.POST["obs"]
            pc.estado = 0 #pasara a 1 cuando cancele todo
            pc.usuario = request.user.username
            pc.fecha_sistema = date.today()
            pc.save()
            messages.success(request, 'Nota de Credito Ingresado Exitosamente! ¡¡Guarde el Numero de Verificador y Numero Venta!!')
            return redirect('NotaCreditoOk',v,vn,n,request.POST["nota"])

    return render(request,"PagoApp/notacredito.html",{'v':v,'vn':vn,'n':n,'t':t,'tp':tp})



def chequeok(request,v,vn,n,t):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        return render(request,"PagoApp/chequeok.html",{'v':v,'n':n,'vn':vn,'t':t})



def tarjetaok(request,v,vn,n):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        return render(request,"PagoApp/tarjetaok.html",{'v':v,'n':n,'vn':vn})  



def depositok(request,v,vn,n):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        return render(request,"PagoApp/depositok.html",{'v':v,'n':n,'vn':vn})



def notacreditok(request,v,vn,n,nota):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        return render(request,"PagoApp/notacreditok.html",{'v':v,'n':n,'vn':vn,'nota':nota})





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
            e.restante = Decimal(request.POST["totalventa"])-(Decimal(request.POST["totalcheque"])+Decimal(request.POST["abono"]))
            e.observacion = request.POST["obs"]
            e.estado = 1
            e.usuario = request.user.username
            e.created = date.today()
            e.updated = date.today()
            e.save()
            messages.success(request, 'Ingreso de Envio Exitoso!')
            return redirect('IniciarVenta') 
        


    return render(request,"PagoApp/enviocheque.html",{'v':v,'cl':cliente,'c':cheque})






def enviostarjeta(request,v,n):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        #print(e.venta,e.nit,e.fecha,e.total_venta,e.tipo_pago,e.total_pago,e.verificador,e.usuario,e.fecha_sistema)

        #datos del cliente
        cliente = Clientes.objects.filter(nit=n)
        #datos del pago en efectivo
        tarjeta = PagoTarjeta.objects.filter(nit=n,verificador=v)
        

        if request.method == "POST":
            e = EnviosTarjeta()
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
            e.numero_tarjeta = request.POST["numerot"]
            e.banco = request.POST["banco"]
            e.total = request.POST["totalventa"]
            e.autorizacion = request.POST["autorizacion"]
            e.observacion = request.POST["obs"]
            e.estado = 1
            e.usuario = request.user.username
            e.created = date.today()
            e.updated = date.today()
            e.save()
            messages.success(request, 'Ingreso de Envio Exitoso!')
            return redirect('IniciarVenta') 
        


    return render(request,"PagoApp/enviotarjeta.html",{'v':v,'cl':cliente,'t':tarjeta})





def enviosdeposito(request,v,n):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        #print(e.venta,e.nit,e.fecha,e.total_venta,e.tipo_pago,e.total_pago,e.verificador,e.usuario,e.fecha_sistema)

        #datos del cliente
        cliente = Clientes.objects.filter(nit=n)
        #datos del pago en efectivo
        deposito = PagoDeposito.objects.filter(nit=n,verificador=v)
        

        if request.method == "POST":
            e = EnviosDeposito()
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
            e.numero_boleta = request.POST["numerob"]
            e.banco = request.POST["banco"]
            e.monto_deposito = request.POST["monto"]
            e.total_venta = request.POST["totalventa"]
            e.observacion = request.POST["obs"]
            e.estado = 1
            e.usuario = request.user.username
            e.created = date.today()
            e.updated = date.today()
            e.save()
            messages.success(request, 'Ingreso de Envio Exitoso!')
            return redirect('IniciarVenta') 
        


    return render(request,"PagoApp/enviodeposito.html",{'v':v,'cl':cliente,'d':deposito})





def enviosnotacredito(request,v,n,nota):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        #print(e.venta,e.nit,e.fecha,e.total_venta,e.tipo_pago,e.total_pago,e.verificador,e.usuario,e.fecha_sistema)

        #datos del cliente
        cliente = Clientes.objects.filter(nit=n)
        #datos del pago en efectivo
        notac = NotaCredito.objects.filter(nit=n,verificador=v)
        

        if request.method == "POST":
            e = EnviosNotaCredito()
            e.verificador = request.POST["verificador"]
            e.notacredito = nota
            e.remitente = request.POST["remitente"]
            e.direccion_remitente = request.POST["dir_remitente"]
            e.telefono_remitente = request.POST["tel_remitente"]
            e.destinatario = request.POST["destinatario"]
            e.nit = request.POST["nit"]
            e.direccion =  request.POST["direccion"]
            e.telefono = request.POST["tel"]
            e.venta = request.POST["venta"]
            e.tipo = request.POST["tipo"]
            e.total_venta = request.POST["totalventa"]
            e.fecha_inicio = request.POST["inicio"]
            e.fecha_fin = request.POST["fin"]
            e.observacion = request.POST["obs"]
            e.estado = 1 #paquete enviado
            e.usuario = request.user.username
            e.created = date.today()
            e.updated = date.today()
            e.save()
            messages.success(request, 'Ingreso de Envio Exitoso!')
            return redirect('IniciarVenta') 
        


    return render(request,"PagoApp/enviocredito.html",{'v':v,'cl':cliente,'n':notac})



