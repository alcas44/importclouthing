from django.db import models


class DatosVenta(models.Model):
    venta = models.BigIntegerField(primary_key=True)
    nit = models.CharField(max_length=14,blank=False)
    fecha_venta = models.CharField(max_length=20,blank=False)
    vendedor = models.CharField(max_length=200,blank=False)
    estado = models.IntegerField(blank=False,default=0)

    class Meta:#nombre que tendran en singular y plural
        verbose_name="venta"
        verbose_name_plural="ventas"

    def __str__(self):
        return self.venta #como va a aparecer en el panel admin  




class Detalle(models.Model):
    venta = models.BigIntegerField(blank=False)
    codigo = models.CharField(max_length=75)
    precio = models.FloatField(blank=False)
    cantidad = models.IntegerField(null=False,default=0)
    total = models.FloatField(blank=False)
    estado = models.IntegerField(null=False,default=0)


    class Meta:#nombre que tendran en singular y plural
        verbose_name="detalle"
        verbose_name_plural="detalles"

    def __str__(self):
        return self.venta #como va a aparecer en el panel admin       