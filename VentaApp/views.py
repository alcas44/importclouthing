from django.shortcuts import render,redirect
from IngresosApp.models import Articulos,Clientes
from datetime import datetime

def iniciarventa(request):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        if request.method == "POST":
            try:
                dato = Clientes.objects.filter(nit=request.POST["dato"])
                fecha = datetime.today()
                return render(request,"VentaApp/buscar.html",{'dato':dato,'f':fecha})
            except:
                dato = "Error"
                return redirect('IniciarVenta')
        else:
            return render(request,"VentaApp/buscar.html")


def catalogo(request):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        pass




def verarticulo(request,id):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        articulos = Articulos.objects.filter(codigo=id)
        return render(request,"VentaApp/articulos.html",{'form':articulos})
