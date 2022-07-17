from IngresosApp import views
from django.urls import path
from django.conf import settings#para agregar la ruta de la imagen 
from django.conf.urls.static import static#para agregar la ruta de la imagen 

urlpatterns = [
    path('articulo/',views.nuevoarticulo,name="NuevoArt"),
    path('cliente/',views.nuevocliente,name="NuevoCliente"),
    #path('envios/',views.nuevoenvio,name="NuevoEnvio"),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)