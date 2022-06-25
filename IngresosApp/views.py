from pyexpat import model
from django.shortcuts import render
from django.views.generic import CreateView

from IngresosApp.models import Articulos,Clientes
from .forms import ArticulosForm,ClientesForm

def nuevoarticulo(request):
    form = ArticulosForm()
    return render(request,"IngresosApp/nuevoart.html",{'form':form})


   
def nuevocliente(request):
    form = ClientesForm()
    return render(request,"IngresosApp/nuevocliente.html",{'form':form})