from ReportesApp import views
from django.urls import path

urlpatterns = [
    path('clientes/<str:id>',views.rclientes,name="ReporteCliente"),
    #path('detallecliente/<str:id>',views.detallecliente,name="DetalleCliente"),
    #path('inventario/',views.inventarioarticulos,name="InventarioArticulos"),
]
