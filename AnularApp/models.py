import datetime
from django.db import models


class DatosAnulacion(models.Model):
    venta = models.BigIntegerField(primary_key=True,blank=False,null=False)
    nit = models.CharField(max_length=14,blank=False)
    cliente = models.CharField(max_length=250,blank=False)
    total_venta = models.DecimalField(max_digits=10,decimal_places=2,blank=False)
    motivo = models.CharField(max_length=850,blank=False,null=False)
    fecha_anulacion = models.DateField(blank=False)
    usuario = models.CharField(max_length=200,blank=False)
    fecha_sistema = models.DateTimeField(blank=False,null=False)


    class Meta:#nombre que tendran en singular y plural
        verbose_name="datosanulacion"
        verbose_name_plural="datosanulaciones"

    def __str__(self):
        return str(self.venta) #como va a aparecer en el panel admin



class DetalleAnulacion(models.Model):
    venta = models.ForeignKey(DatosAnulacion,on_delete=models.CASCADE)
    nit = models.CharField(max_length=14,blank=False)
    codigo = models.CharField(max_length=75)
    precio = models.DecimalField(max_digits=10,decimal_places=2, blank=False)
    cantidad = models.IntegerField(null=False,default=0)
    total = models.DecimalField(max_digits=10,decimal_places=2, blank=False)
    estado = models.IntegerField(null=False,default=0)
    fecha_anulacion = models.DateField(blank=False)
    usuario = models.CharField(max_length=200,blank=False)
    fecha_sistema = models.DateTimeField(blank=False)


    class Meta:#nombre que tendran en singular y plural
        verbose_name="detalleanulacion"
        verbose_name_plural="detalleanulaciones"

    def __str__(self):
        return str(self.venta) #como va a aparecer en el panel admin      