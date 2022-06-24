from InicioAsesor import views
from django.urls import path

urlpatterns = [
    path('',views.inicioasesor,name="InicioAsesor"),
]
