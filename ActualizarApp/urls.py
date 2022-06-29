from ActualizarApp import views
from django.urls import path
from django.conf import settings#para agregar la ruta de la imagen 
from django.conf.urls.static import static#para agregar la ruta de la imagen 

urlpatterns = [
    path('actualizar-articulo/<str:id>',views.actualizararti,name="ActualizarArt"),
    path('actualizar-cliente/<str:id>',views.actualizarcliente,name="ActualizarCliente"),
    #path('actualizar-envios/',views.nuevoenvio,name="NuevoEnvio"),
    path('ver-articulo/',views.verarti,name="VerArticulos"),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)