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
    if not request.user.is_authenticated and not request.user.is_active:
        redirect('/')
    else:    
        form = ClientesForm()
        if request.method == "POST":
            form = ClientesForm(request.POST)
            if form.is_valid():
              try:
                data = Clientes()
                data.codigo = form.cleaned_data['codigo']
                data.nit = form.cleaned_data['nit']
                data.tipo = form.cleaned_data['tipo']
                data.nombres = form.cleaned_data['nombres']
                data.apellidos = form.cleaned_data['apellidos']
                data.direccion = form.cleaned_data['direccion']
                data.telefono = form.cleaned_data['telefono']
                data.correo = form.cleaned_data['correo']
                data.fecha_nac = form.cleaned_data['fecha_nac']
                data.cuenta = 0.00
                data.usuario =  request.user
                data.created = datetime.today()
                data.updated = datetime.today()
                data.save()
                return redirect('NuevoCliente')
              except:
                m=messages.info(request,"No ha completado la informacion")
                return render(request,"IngresosApp/nuevocliente.html",{'form':form})
                
        return render(request,"IngresosApp/nuevocliente.html",{'form':form})



def nuevoenvio(request):
     if not request.user.is_authenticated and not request.user.is_active:
        redirect('/')
     else:    
        form = EnviosForm()
        if request.method == "POST":
            form = EnviosForm(request.POST)
            if form.is_valid():
              try:
                data = Envios()
                data.codigo = form.cleaned_data["codigo"]
                data.tipo = form.cleaned_data["tipo"]
                data.remitente = form.cleaned_data["remitente"]
                data.destinatario = form.cleaned_data["destinatario"]
                data.direccion = form.cleaned_data["direccion"]
                data.telefono = form.cleaned_data["telefono"]
                data.estado = form.cleaned_data["estado"]
                data.monto = form.cleaned_data["monto"]
                data.guia = form.cleaned_data["guia"]
                data.observacion = form.cleaned_data["observacion"]
                data.usuario = request.user
                data.created = datetime.today()
                data.updated = datetime.today()
                data.save()                
                return redirect('NuevoEnvio')
              except:
                return render(request,"IngresosApp/nuevoenvio.html",{'form':form})
                
        return render(request,"IngresosApp/nuevoenvio.html",{'form':form})