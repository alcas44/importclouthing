from django.contrib import messages
from django.shortcuts import render,redirect
from IngresosApp.models import Articulos,Clientes
from IngresosApp.forms import ArticulosForm,ClientesForm

def updatearticulo(request,id):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
         articulo = Articulos.objects.get(codigo=id)
         if request.method == 'GET':
            form = ArticulosForm(instance=articulo)
         else:
            form = ArticulosForm(request.POST,instance = articulo)
     
            if form.is_valid():
                try:
                    form.save()
                    messages.success(request, 'Articulo Modificado Exitosamente!.')
                    return redirect('InventarioArticulos')#la redireccion es en name del path en la url  path('',views.compras,name="Compras"),
                except:
                    messages.error(request, 'Modificacion de Articulos Fallido!.')
                    return redirect('InventarioArticulos') # path('error/',views.error,name="Error"),

    
    return render(request,"ActualizarApp/articulos.html",{'form':form})               




def updatecliente(request,id):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
         cliente = Clientes.objects.get(nit=id)
         if request.method == 'GET':
            form = ClientesForm(instance=cliente)
         else:
            form = ClientesForm(request.POST,instance = cliente)
     
            if form.is_valid():
                try:
                    form.save()
                    messages.success(request, 'Cliente Modificado Exitosamente!.')
                    return redirect('InventarioClientes')#la redireccion es en name del path en la url  path('',views.compras,name="Compras"),
                except:
                    messages.error(request, 'Modificacion de Cliente Fallida!.')
                    return redirect('Inventarioclientes') # path('error/',views.error,name="Error"),

    
    return render(request,"ActualizarApp/clientes.html",{'form':form})               

