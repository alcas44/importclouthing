"""tienda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings#para agregar la ruta de la imagen 
from django.conf.urls.static import static#para agregar la ruta de la imagen 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("LoginApp.urls")),
    path('inicio/',include("InicioAdmin.urls")),
    path('ingresos/',include("IngresosApp.urls")),
    path('inventario/',include("InventariosApp.urls")),
    path('ver/',include("VerApp.urls")),
    path('modificar/',include("ActualizarApp.urls")),
    path('borrar/',include("BorrarApp.urls")),
    path('venta/',include("VentaApp.urls")),
    path('reportes/',include("ReportesApp.urls")),
    path('pago/',include("PagoApp.urls")),
    path('anular/',include("AnularApp.urls")),
    #Urls Asesores de Ventas
    path('asesor/',include("InicioAsesor.urls")),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)