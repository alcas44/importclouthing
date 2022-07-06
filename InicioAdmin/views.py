from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from IngresosApp.models import Articulos,Clientes
from VentaApp.models import Detalle
from django.db.models import Sum

@login_required
def inicioadmin(request):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        articulos = Articulos.objects.all().count()#es para saber cuantos articulos hay 
        clientes = Clientes.objects.all().count()#es para saber cuantos clientes hay
        lastartis = Articulos.objects.all()[:3]#es para saber el top 3 de los ultimos ingresos
        total = Detalle.objects.all().aggregate(tot=Sum('total'))
        
        return render(request,"InicioAdmin/inicio.html",{'articulos':articulos,'clientes':clientes,'top3':lastartis,'total':total})


            
