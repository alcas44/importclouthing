from django.shortcuts import render,redirect
from IngresosApp.models import Clientes,Envios
from VentaApp.models import DatosVenta,Detalle
from PagoApp.models import NotaCredito, PagoCheque, PagoDeposito, PagoEfectivo, PagoTarjeta
from django.db.models import Sum




def rclientes(request,id):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        #obtenemos el cliente
        ver = Clientes.objects.get(nit=id)

        #totales
        totales = Detalle.objects.filter(nit=id).aggregate(tot=Sum('total'))
        total_efe = PagoEfectivo.objects.filter(nit=id).count()
        total_tar = PagoTarjeta.objects.filter(nit=id).count()
        total_che = PagoCheque.objects.filter(nit=id).count()
        total_dep = PagoDeposito.objects.filter(nit=id).count()
        total_cre = NotaCredito.objects.filter(nit=id).count()


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



        return render(request,"ReportesApp/clientes.html",{'ver':ver,'vc':vc,'total':totales,'te':total_efe,'tt':total_tar,'tc':total_che,'td':total_dep,'nc':total_cre,'n':id})




def renvios(request,n):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        ver = Envios.objects.filter(nit=n)
        
      
       
    
    return render(request,"ReportesApp/envios.html",{'ver':ver})




def refectivo(request,n):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        ver = PagoEfectivo.objects.filter(nit=n)
            #obtenemos el cliente
        cli = Clientes.objects.get(nit=n)
      
       
    
    return render(request,"ReportesApp/efectivo.html",{'ver':ver,'cl':cli})




def rtarjeta(request,n):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        ver = PagoTarjeta.objects.filter(nit=n)
            #obtenemos el cliente
        cli = Clientes.objects.get(nit=n)
      
       
    
    return render(request,"ReportesApp/tarjeta.html",{'ver':ver,'cl':cli})  





def rcheque(request,n):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        ver = PagoCheque.objects.filter(nit=n)
            #obtenemos el cliente
        cli = Clientes.objects.get(nit=n)
      
       
    
    return render(request,"ReportesApp/cheque.html",{'ver':ver,'cl':cli})    





def rdeposito(request,n):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        ver = PagoDeposito.objects.filter(nit=n)
            #obtenemos el cliente
        cli = Clientes.objects.get(nit=n)
      
       
    
    return render(request,"ReportesApp/deposito.html",{'ver':ver,'cl':cli})  





def rcredito(request,n):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        ver = NotaCredito.objects.filter(nit=n)
            #obtenemos el cliente
        cli = Clientes.objects.get(nit=n)
      
       
    
    return render(request,"ReportesApp/notacredito.html",{'ver':ver,'cl':cli})               




     
