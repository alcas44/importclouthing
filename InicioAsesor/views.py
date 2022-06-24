from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

@login_required
def inicioasesor(request):
    if not request.user.is_authenticated and not request.user.is_active and request.user.rol == 'asesor':
        return redirect('/')
    else:
        return render(request,"InicioAsesor/inicio.html")
