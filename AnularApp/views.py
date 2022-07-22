from django.shortcuts import render,redirect
from IngresosApp.models import Clientes
from VentaApp.models import DatosVenta,Detalle
from django.db.models import Sum

def anularventa(request):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        
        #obtenemos todas las ventas
        venta = DatosVenta.objects.all().select_related("nit")
     

        return render(request,"AnularApp/listaventas.html",{'v':venta})
