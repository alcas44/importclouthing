import imp
from django.shortcuts import render,redirect
from IngresosApp.models import Clientes
from VentaApp.models import DatosVenta,Detalle




def rclientes(request,id):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        ver = Clientes.objects.get(nit=id)
        vc = DatosVenta.objects.filter(nit_id=ver.id)
        return render(request,"ReportesApp/clientes.html",{'ver':ver,'vc':vc})



     
