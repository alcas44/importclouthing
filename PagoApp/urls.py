from PagoApp import views
from django.urls import path
from django.conf import settings#para agregar la ruta de la imagen 
from django.conf.urls.static import static#para agregar la ruta de la imagen 

urlpatterns = [
    path('<int:id>/<str:n>',views.pago,name="Pago"),
    path('efectivo/<int:v>/<str:n>',views.efectivo,name="Efectivo"),

    path('cheque/<int:v>/<int:vn>/<str:n>/<str:t>/<str:tp>',views.cheque,name="Cheque"),
    path('cheque/<int:v>/<int:vn>/<str:n>',views.chequeok,name="ChequeOk"),

    path('tarjeta/<int:v>/<int:vn>/<str:n>/<str:t>/<str:tp>',views.tarjeta,name="Tarjeta"),
    path('tarjeta/<int:v>/<int:vn>/<str:n>',views.tarjetaok,name="TarjetaOk"),

    path('deposito/<int:v>/<int:vn>/<str:n>/<str:t>/<str:tp>',views.deposito,name="Deposito"),
    path('deposito/<int:v>/<int:vn>/<str:n>',views.depositok,name="DepositoOk"),

    path('envios/<int:v>/<str:n>',views.envios,name="Envios"),
    path('envio/<int:v>/<str:n>',views.envioscheque,name="Envios2"),
    path('enviot/<int:v>/<str:n>',views.enviostarjeta,name="Envios3"),
    path('enviodepo/<int:v>/<str:n>',views.enviosdeposito,name="EnviosDepo"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)