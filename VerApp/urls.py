from VerApp import views
from django.urls import path

urlpatterns = [
    path('articulo/<str:id>',views.verarticulo,name="VerArticulo"),
    #path('clientes/',views.inventariocliente,name="InventarioClientes"),
]
