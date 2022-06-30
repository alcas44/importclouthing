from ActualizarApp import views
from django.urls import path

urlpatterns = [
    path('articulo/<str:id>',views.updatearticulo,name="UpdateArticulo"),
    path('clientes/<str:id>',views.updatecliente,name="UpdateCliente"),
]
