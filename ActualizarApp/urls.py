from ActualizarApp import views
from django.urls import path
from django.conf import settings#para agregar la ruta de la imagen 
from django.conf.urls.static import static#para agregar la ruta de la imagen 

urlpatterns = [
    path('articulo/<str:id>',views.updatearticulo,name="UpdateArticulo"),
    path('clientes/<str:id>',views.updatecliente,name="UpdateCliente"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)