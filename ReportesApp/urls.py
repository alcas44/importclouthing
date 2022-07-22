from ReportesApp import views
from django.urls import path

urlpatterns = [
    path('clientes/<str:id>',views.rclientes,name="ReporteCliente"),
    path('envios/<str:n>',views.renvios,name="ReporteEnvios"),
    path('reportefectivo/<str:n>',views.refectivo,name="RE"),
    path('reportecheque/<str:n>',views.rcheque,name="RC"),
    path('reportetarjeta/<str:n>',views.rtarjeta,name="RT"),
    path('reportedeposito/<str:n>',views.rdeposito,name="RD"),
    path('reportecredito/<str:n>',views.rcredito,name="RNC"),
]
