from VentaApp import views
from django.urls import path
from django.conf import settings#para agregar la ruta de la imagen 
from django.conf.urls.static import static#para agregar la ruta de la imagen 

urlpatterns = [
    path('',views.iniciar,name="IniciarVenta"),
    path('agregar/<int:id>/<str:n>',views.venta,name="Venta"),
    path('finalizar/<int:id>/<str:n>',views.fin_venta,name="FinVenta")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)