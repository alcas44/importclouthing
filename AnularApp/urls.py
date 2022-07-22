from AnularApp import views
from django.urls import path
from django.conf import settings#para agregar la ruta de la imagen 
from django.conf.urls.static import static#para agregar la ruta de la imagen 

urlpatterns = [
    path('venta/',views.anularventa,name="AnularVenta"),
    #path('clientes/<str:id>',views.updatecliente,name="UpdateCliente"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)