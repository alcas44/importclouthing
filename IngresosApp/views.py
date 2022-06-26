from django.contrib import messages
from django.shortcuts import render,redirect
from IngresosApp.models import Articulos,Clientes,Envios
from .forms import ArticulosForm,ClientesForm,EnviosForm
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
                data = Articulos()#tabla a guarda los datos
                data.codigo = form.cleaned_data['codigo']
                data.referencia = form.cleaned_data['referencia']
                data.descripcion = form.cleaned_data['descripcion']
                data.marca = form.cleaned_data['marca']
                data.precio_compra = form.cleaned_data['precio_compra']
                data.precio_venta = form.cleaned_data['precio_venta']
                data.descuento = form.cleaned_data['descuento']
                data.existencia = form.cleaned_data['existencia']
                data.imagen = form.cleaned_data['imagen']
                data.usuario = request.user
                data.created = datetime.today()
                data.updated = datetime.today()
                data.save()
                return redirect('NuevoArt')
              except:
                return redirect('/')
                
        return render(request,"IngresosApp/nuevoart.html",{'form':form})


   
def nuevocliente(request):
    form = ClientesForm()
    return render(request,"IngresosApp/nuevocliente.html",{'form':form})



def nuevoenvio(request):
    form = EnviosForm()
    return render(request,"IngresosApp/nuevoenvio.html",{'form':form})