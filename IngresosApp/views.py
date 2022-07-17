
from django.contrib import messages
from django.shortcuts import render,redirect,HttpResponse
from IngresosApp.models import Articulos,Clientes,Envios
from .forms import ArticulosForm,ClientesForm
from datetime import datetime

def nuevoarticulo(request):
    if not request.user.is_authenticated and not request.user.is_active:
        redirect('/')
    else:    
        form = ArticulosForm()
        if request.method == "POST":
            form = ArticulosForm(request.POST,request.FILES)
            if form.is_valid():
                try:
                  ver = Articulos.objects.filter(codigo=request.POST['codigo'])
                  if(ver):
                    messages.error(request, 'Este Articulo Ya Existe.')
                    return redirect('NuevoArt') 
                  else:
                    data = Articulos()#tabla a guarda los datos
                    data.codigo = form.cleaned_data['codigo']
                    data.referencia = form.cleaned_data['referencia']
                    data.descripcion = form.cleaned_data['descripcion']
                    data.color = form.cleaned_data['color']
                    data.marca = form.cleaned_data['marca']
                    data.precio_compra = form.cleaned_data['precio_compra']
                    data.precio_venta = form.cleaned_data['precio_venta']
                    data.existencia = form.cleaned_data['existencia']
                    data.imagen = form.cleaned_data['imagen']
                    data.usuario = request.user
                    data.created = datetime.today()
                    data.updated = datetime.today()
                    data.save()
                    messages.success(request, 'Articulo Ingresado Exitosamente!.')
                    return redirect('NuevoArt')  
                except:
                   messages.error(request, 'Error al Ingresar Articulo !')
                   return render(request,"IngresosApp/nuevoart.html",{'form':form})      
        
        return render(request,"IngresosApp/nuevoart.html",{'form':form})


   
def nuevocliente(request):
    if not request.user.is_authenticated and not request.user.is_active:
        redirect('/')
    else:    
        form = ClientesForm()
        if request.method == "POST":
            form = ClientesForm(request.POST)
            if form.is_valid():
              try:
                ver = Clientes.objects.filter(nit=request.POST['nit'])
                if(ver):
                    messages.error(request, 'Este Cliente Ya Existe.')
                    return redirect('NuevoCliente')
                else:
                  data = Clientes()
                  data.nit = form.cleaned_data['nit']
                  data.negocio = form.cleaned_data['negocio']
                  data.nombres = form.cleaned_data['nombres']
                  data.apellidos = form.cleaned_data['apellidos']
                  data.direccion = form.cleaned_data['direccion']
                  data.telefono = form.cleaned_data['telefono']
                  data.telefono2 = form.cleaned_data['telefono2']
                  data.correo = form.cleaned_data['correo']
                  data.cuenta = 0.00
                  data.usuario =  request.user
                  data.created = datetime.today()
                  data.updated = datetime.today()
                  data.save()
                  messages.success(request, 'Cliente Ingresado Exitosamente!.')
                  return redirect('NuevoCliente')
              except:
                return render(request,"IngresosApp/nuevocliente.html",{'form':form})
                
        return render(request,"IngresosApp/nuevocliente.html",{'form':form})



