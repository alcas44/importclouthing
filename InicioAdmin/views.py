from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from IngresosApp.models import Articulos

@login_required
def inicioadmin(request):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'admin':
        return redirect('/')
    else:
        conteo = Articulos.objects.all().count()
        return render(request,"InicioAdmin/inicio.html",{'conteo':conteo})


            
