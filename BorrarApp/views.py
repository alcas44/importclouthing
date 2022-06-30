from django.contrib import messages
from django.shortcuts import render,redirect
from IngresosApp.models import Articulos,Clientes
from IngresosApp.forms import ArticulosForm,ClientesForm

def deletearticulo(request,id):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
         articulo = Articulos.objects.get(codigo=id)
         if request.method == 'GET':
            try:
                    articulo.delete()
                    messages.success(request, 'Articulo Eliminado Exitosamente!.')
                    return redirect('InventarioArticulos')#la redireccion es en name del path en la url  path('',views.compras,name="Compras"),
            except:
                    messages.error(request, 'Eliminacion de Articulo Fallido!.')
                    return redirect('InventarioArticulos') # path('error/',views.error,name="Error"),
         else:
                try:
                    articulo.delete()
                    messages.success(request, 'Articulo Eliminado Exitosamente!.')
                    return redirect('InventarioArticulos')#la redireccion es en name del path en la url  path('',views.compras,name="Compras"),
                except:
                    messages.error(request, 'Eliminacion de Articulo Fallido!.')
                    return redirect('InventarioArticulos') # path('error/',views.error,name="Error"),
        




def deletecliente(request,id):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
         cliente = Clientes.objects.get(nit=id)
         if request.method == 'GET':
            try:
                    cliente.delete()
                    messages.success(request, 'Cliente Eliminado Exitosamente!.')
                    return redirect('InventarioClientes')#la redireccion es en name del path en la url  path('',views.compras,name="Compras"),
            except:
                    messages.error(request, 'Eliminacion de Cliente Fallido!.')
                    return redirect('InventarioClientes') # path('error/',views.error,name="Error"),
            
         else:
            
                try:
                    cliente.delete()
                    messages.success(request, 'Cliente Eliminado Exitosamente!.')
                    return redirect('InventarioClientes')#la redireccion es en name del path en la url  path('',views.compras,name="Compras"),
                except:
                    messages.error(request, 'Eliminacion de Cliente Fallida!.')
                    return redirect('InventarioClientes') # path('error/',views.error,name="Error"),
 