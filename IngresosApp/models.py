from email.policy import default
from enum import unique
from unicodedata import digit
from django.db import models
from django.forms import EmailField


class Articulos(models.Model):
    codigo=models.CharField(max_length=75,blank=False)
    referencia=models.CharField(max_length=200,blank=False)
    descripcion=models.CharField(max_length=200,blank=False)
    marca=models.CharField(max_length=200,blank=False)
    precio_compra=models.FloatField(blank=False)
    precio_venta=models.FloatField(blank=False)
    descuento=models.FloatField(null=True)
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
    codigo=models.CharField(max_length=75,blank=False)
    nit=models.CharField(max_length=14,blank=False)
    tipo=models.CharField(max_length=50,blank=False)
    nombres=models.CharField(max_length=200,blank=False)
    apellidos=models.CharField(max_length=200,blank=False)
    direccion=models.CharField(max_length=500,blank=False)
    telefono=models.CharField(max_length=9,blank=False)
    correo=models.CharField(max_length=250,blank=True)
    fecha_nac=models.DateField(blank=True)
    cuenta=models.FloatField()
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
    codigo=models.CharField(max_length=75,blank=False)
    tipo=models.CharField(max_length=200,blank=False)
    remitente=models.CharField(max_length=200,blank=False)
    destinatario=models.CharField(max_length=200,blank=False)
    direccion=models.CharField(max_length=500,blank=False)
    telefono=models.CharField(max_length=9,blank=False)
    estado=models.CharField(max_length=75,blank=False)
    monto=models.FloatField(blank=True)
    guia=models.CharField(max_length=100,blank=True)
    observacion=models.CharField(max_length=500,blank=True)
    usuario=models.CharField(max_length=200,blank=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:#nombre que tendran en singular y plural
        verbose_name="envios"
        verbose_name_plural="envios"

    def __str__(self):
        return self.codigo #como va a aparecer en el panel admin   
