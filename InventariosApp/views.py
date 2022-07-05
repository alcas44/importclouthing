from itertools import count
from django.shortcuts import render,redirect
from IngresosApp.models import Articulos,Clientes
from VentaApp.models import Detalle,DatosVenta

def inventarioarti(request):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        articulos = Articulos.objects.all()
        return render(request,"InventariosApp/articulos.html",{'art':articulos})


def inventariocliente(request):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        clientes = Clientes.objects.all()
        return render(request,"InventariosApp/clientes.html",{'art':clientes})
