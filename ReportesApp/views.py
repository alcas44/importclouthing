from cgi import print_arguments
import imp
from django.shortcuts import render,redirect
from IngresosApp.models import Clientes,Envios
from VentaApp.models import DatosVenta,Detalle
from PagoApp.models import NotaCredito, PagoCheque, PagoDeposito, PagoEfectivo, PagoTarjeta




def rclientes(request,id):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        #obtenemos el cliente
        ver = Clientes.objects.get(nit=id)
        
        #datos de pago en efectivo
        efectivo = PagoEfectivo.objects.filter(nit=id)
        
        #datos de pago en tarjeta
        tarjeta = PagoTarjeta.objects.filter(nit=id)

        #dato de pago en cheque
        cheque = PagoCheque.objects.filter(nit=id)

        #dato de pago en deposito
        deposito = PagoDeposito.objects.filter(nit=id)

        #dato de pago nota de credito
        credito = NotaCredito.objects.filter(nit=id)

        vc = DatosVenta.objects.filter(nit_id=ver.id)



        return render(request,"ReportesApp/clientes.html",{'ver':ver,'vc':vc})




def renvios(request,n):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        ver = Envios.objects.filter(nit=n)
        
      
       
    
    return render(request,"ReportesApp/envios.html",{'ver':ver})        



     
