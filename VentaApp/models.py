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