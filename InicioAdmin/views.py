from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from IngresosApp.models import Articulos,Clientes

@login_required
def inicioadmin(request):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        articulos = Articulos.objects.all().count()
        clientes = Clientes.objects.all().count()
        lastartis = Articulos.objects.all()[:3]
        return render(request,"InicioAdmin/inicio.html",{'articulos':articulos,'clientes':clientes,'top3':lastartis})


            
