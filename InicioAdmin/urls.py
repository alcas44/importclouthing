from InicioAdmin import views
from django.urls import path

urlpatterns = [
    path('',views.inicioadmin,name="InicioAdmin"),
]
