from VerApp import views
from django.urls import path

urlpatterns = [
    path('articulo/<str:id>',views.verarticulo,name="VerArticulo"),
    path('clientes/<str:id>',views.vercliente,name="VerCliente"),
    path('envios/<str:id>/<int:v>',views.verenvio,name="VerEnvio"),
]
