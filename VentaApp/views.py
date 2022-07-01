from django.shortcuts import render,redirect
from IngresosApp.models import Articulos,Clientes
from datetime import datetime

contador = 0

def iniciarventa(request):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        global contador
        if request.method == "POST":
            try:
                dato = Clientes.objects.filter(nit=request.POST["dato"])
                fecha = datetime.today()
                contador = contador + 1 # hacer que aumente despues del save hacer un if para que acumule
                return render(request,"VentaApp/buscar.html",{'dato':dato,'f':fecha,'c':contador})
            except:
                dato = "Error"
                contador = contador - 1
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
