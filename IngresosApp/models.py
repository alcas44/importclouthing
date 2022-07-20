from email.policy import default
from enum import unique
from unicodedata import digit
from django.db import models
from django.forms import EmailField


class Articulos(models.Model):
    codigo=models.CharField(max_length=75)
    referencia=models.CharField(max_length=200,blank=False)
    descripcion=models.CharField(max_length=200,blank=False)
    color=models.CharField(max_length=50,blank=False)
    marca=models.CharField(max_length=200,blank=False)
    precio_compra=models.DecimalField(max_digits=10,decimal_places=2, blank=False)
    precio_venta=models.DecimalField(max_digits=10,decimal_places=2, blank=False)
    existencia=models.IntegerField(null=False,default=0)
    imagen=models.ImageField(upload_to="articulos",null=True,blank=True)
    usuario=models.CharField(max_length=200,blank=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:#nombre que tendran en singular y plural
        verbose_name="articulo"
        verbose_name_plural="articulos"

    def __str__(self):
        return self.codigo #como va a aparecer en el panel admin   






# Modelo Cliente

class Clientes(models.Model):
    nit=models.CharField(max_length=14,blank=True,null=True)
    negocio=models.CharField(max_length=50,blank=False)
    nombres=models.CharField(max_length=200,blank=False)
    apellidos=models.CharField(max_length=200,blank=False)
    direccion=models.CharField(max_length=500,blank=False)
    telefono=models.CharField(max_length=9,blank=False)
    telefono2=models.CharField(max_length=9,blank=False)
    correo=models.CharField(max_length=250,blank=True)
    usuario=models.CharField(max_length=200,blank=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:#nombre que tendran en singular y plural
        verbose_name="cliente"
        verbose_name_plural="clientes"

    def __str__(self):
        return self.nit #como va a aparecer en el panel admin   





# Modelo Envios

class Envios(models.Model):
    verificador=models.IntegerField(primary_key=True,blank=False,null=False)
    remitente=models.CharField(max_length=250,blank=False)
    direccion_remitente=models.CharField(max_length=250,blank=False)
    telefono_remitente=models.CharField(max_length=9,blank=False)
    destinatario=models.CharField(max_length=250,blank=False)
    nit=models.CharField(max_length=14,blank=False)
    direccion=models.CharField(max_length=500,blank=False)
    telefono=models.CharField(max_length=9,blank=False)
    venta=models.CharField(max_length=100,blank=False)
    tipo=models.CharField(max_length=75,blank=False)
    monto=models.DecimalField(max_digits=10,decimal_places=2, blank=False)
    total=models.DecimalField(max_digits=10,decimal_places=2, blank=False)
    observacion=models.CharField(max_length=500,blank=True)
    estado=models.CharField(max_length=75,blank=False)
    usuario=models.CharField(max_length=200,blank=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:#nombre que tendran en singular y plural
        verbose_name="envios"
        verbose_name_plural="envios"

    def __str__(self):
        return self.verificador #como va a aparecer en el panel admin   




class EnviosCheque(models.Model):
    verificador=models.IntegerField(primary_key=True,blank=False,null=False)
    remitente=models.CharField(max_length=250,blank=False)
    direccion_remitente=models.CharField(max_length=250,blank=False)
    telefono_remitente=models.CharField(max_length=9,blank=False)
    destinatario=models.CharField(max_length=250,blank=False)
    nit=models.CharField(max_length=14,blank=False)
    direccion=models.CharField(max_length=500,blank=False)
    telefono=models.CharField(max_length=9,blank=False)
    venta=models.CharField(max_length=100,blank=False)
    tipo=models.CharField(max_length=75,blank=False)
    numero_cheque=models.IntegerField(blank=False)
    banco=models.CharField(max_length=250,blank=False)
    fecha_cheque=models.CharField(max_length=75,blank=False)
    total=models.DecimalField(max_digits=10,decimal_places=2, blank=False)
    abono=models.DecimalField(max_digits=10,decimal_places=2, blank=False)
    restante=models.DecimalField(max_digits=10,decimal_places=2, blank=False)
    observacion=models.CharField(max_length=500,blank=True)
    estado=models.CharField(max_length=75,blank=False)
    usuario=models.CharField(max_length=200,blank=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:#nombre que tendran en singular y plural
        verbose_name="enviocheque"
        verbose_name_plural="enviocheques"

    def __str__(self):
        return self.verificador #como va a aparecer en el panel admin 





class EnviosTarjeta(models.Model):
    verificador=models.IntegerField(primary_key=True,blank=False,null=False)
    remitente=models.CharField(max_length=250,blank=False)
    direccion_remitente=models.CharField(max_length=250,blank=False)
    telefono_remitente=models.CharField(max_length=9,blank=False)
    destinatario=models.CharField(max_length=250,blank=False)
    nit=models.CharField(max_length=14,blank=False)
    direccion=models.CharField(max_length=500,blank=False)
    telefono=models.CharField(max_length=9,blank=False)
    venta=models.CharField(max_length=100,blank=False)
    tipo=models.CharField(max_length=75,blank=False)
    numero_tarjeta=models.IntegerField(blank=False)
    banco=models.CharField(max_length=250,blank=False)
    total=models.DecimalField(max_digits=10,decimal_places=2, blank=False)
    autorizacion=models.IntegerField(blank=False)
    observacion=models.CharField(max_length=500,blank=True)
    estado=models.CharField(max_length=75,blank=False)
    usuario=models.CharField(max_length=200,blank=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:#nombre que tendran en singular y plural
        verbose_name="enviotarjeta"
        verbose_name_plural="enviotarjetas"

    def __str__(self):
        return self.verificador #como va a aparecer en el panel admin        






class EnviosDeposito(models.Model):
    verificador=models.IntegerField(primary_key=True,blank=False,null=False)
    remitente=models.CharField(max_length=250,blank=False)
    direccion_remitente=models.CharField(max_length=250,blank=False)
    telefono_remitente=models.CharField(max_length=9,blank=False)
    destinatario=models.CharField(max_length=250,blank=False)
    nit=models.CharField(max_length=14,blank=False)
    direccion=models.CharField(max_length=500,blank=False)
    telefono=models.CharField(max_length=9,blank=False)
    venta=models.CharField(max_length=100,blank=False)
    tipo=models.CharField(max_length=75,blank=False)
    numero_boleta=models.IntegerField(blank=False)
    banco=models.CharField(max_length=250,blank=False)
    monto_deposito=models.DecimalField(max_digits=10,decimal_places=2, blank=False)
    total_venta=models.DecimalField(max_digits=10,decimal_places=2, blank=False)
    observacion=models.CharField(max_length=500,blank=True)
    estado=models.CharField(max_length=75,blank=False)
    usuario=models.CharField(max_length=200,blank=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:#nombre que tendran en singular y plural
        verbose_name="enviosdeposito"
        verbose_name_plural="enviosdepositos"

    def __str__(self):
        return self.verificador #como va a aparecer en el panel admin                