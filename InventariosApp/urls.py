from InventariosApp import views
from django.urls import path

urlpatterns = [
    path('articulos/',views.inventarioarti,name="InventarioArticulos"),
    path('clientes/',views.inventariocliente,name="InventarioClientes"),
    #path('detallecliente/<str:id>',views.detallecliente,name="DetalleCliente"),
    #path('inventario/',views.inventarioarticulos,name="InventarioArticulos"),
]
