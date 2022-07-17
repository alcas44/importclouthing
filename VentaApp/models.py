from tkinter import CASCADE
from django.db import models
from IngresosApp.models import Clientes


class DatosVenta(models.Model):
    venta = models.BigIntegerField(primary_key=True,default=0)
    nit = models.ForeignKey(Clientes,on_delete=models.CASCADE,null=True)
    fecha_venta = models.CharField(max_length=20,blank=False)
    vendedor = models.CharField(max_length=200,blank=False)
    estado = models.IntegerField(blank=False,default=0)

    class Meta:#nombre que tendran en singular y plural
        verbose_name="venta"
        verbose_name_plural="ventas"

    def __str__(self):
        return str(self.venta) #como va a aparecer en el panel admin  




class Detalle(models.Model):
    venta = models.ForeignKey(DatosVenta,on_delete=models.CASCADE)
    codigo = models.CharField(max_length=75)
    nit = models.CharField(max_length=14,blank=False)
    precio = models.DecimalField(max_digits=10,decimal_places=2, blank=False)
    cantidad = models.IntegerField(null=False,default=0)
    total = models.DecimalField(max_digits=10,decimal_places=2, blank=False)
    estado = models.IntegerField(null=False,default=0)


    class Meta:#nombre que tendran en singular y plural
        verbose_name="detalle"
        verbose_name_plural="detalles"

    def __str__(self):
        return str(self.venta) #como va a aparecer en el panel admin       