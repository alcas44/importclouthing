from django.db import models
from django.forms import CharField

class DatosVenta(models.Model):
    venta = models.BigIntegerField(primary_key=True)
    nit = models.CharField(max_length=14,blank=False)
    negocio = models.CharField(max_length=50,blank=False)
    direccion = models.CharField(max_length=500,blank=False)
    fecha_venta = models.CharField(max_length=9,blank=False)
    vendedor = models.CharField(max_length=20,blank=False)
    estado = models.IntegerField(blank=False,default=0)
