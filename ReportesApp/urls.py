from ReportesApp import views
from django.urls import path

urlpatterns = [
    path('clientes/<str:id>',views.rclientes,name="ReporteCliente"),
    
]
