from PagoApp import views
from django.urls import path
from django.conf import settings#para agregar la ruta de la imagen 
from django.conf.urls.static import static#para agregar la ruta de la imagen 

urlpatterns = [
    path('<int:id>/<str:n>',views.pago,name="Pago"),
    path('efectivo/<int:v>/<str:n>',views.efectivo,name="Efectivo"),
    path('cheque/<int:v>/<int:vn>/<str:n>/<str:t>/<str:tp>',views.cheque,name="Cheque"),
    path('envios/<int:v>/<str:n>',views.envios,name="Envios"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)