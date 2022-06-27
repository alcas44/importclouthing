from HistorialApp import views
from django.urls import path

urlpatterns = [
    path('',views.historialcliente,name="HistorialCliente"),
    path('detallecliente/<int:id>',views.detallecliente,name="DetalleCliente"),
]
