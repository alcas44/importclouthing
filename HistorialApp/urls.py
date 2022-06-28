from HistorialApp import views
from django.urls import path

urlpatterns = [
    path('',views.historialcliente,name="HistorialCliente"),
    path('detallecliente/<str:id>',views.detallecliente,name="DetalleCliente"),
    path('inventario/',views.inventarioarticulos,name="InventarioArticulos"),
]
