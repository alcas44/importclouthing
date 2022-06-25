from pyexpat import model
from django.shortcuts import render
from django.views.generic import CreateView

from IngresosApp.models import Articulos
from .forms import ArticulosForm

def nuevoarticulo(request):
    form = ArticulosForm()
    return render(request,"IngresosApp/nuevoart.html",{'form':form})
