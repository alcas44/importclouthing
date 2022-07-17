from tkinter import CASCADE
from django.db import models
from VentaApp.models import DatosVenta

class PagoEfectivo(models.Model):
    venta = models.BigIntegerField(primary_key=True,null=False)
    nit = models.CharField(max_length=14,blank=False,null=False)
    fecha = models.CharField(max_length=25,blank=False,null=False)
    total_venta = models.DecimalField(max_digits=10,decimal_places=2,blank=False)
    tipo_pago = models.CharField(max_length=75,blank=False,null=False)
    total_pago = models.DecimalField(max_digits=10,decimal_places=2,blank=False,null=False)
    verificador = models.IntegerField()
    usuario = models.CharField(max_length=200,blank=False)
    fecha_sistema = models.DateTimeField(blank=False,null=False)

    class Meta:#nombre que tendran en singular y plural
        verbose_name="pagoefectivo"
        verbose_name_plural="pagoefectivos"

    def __str__(self):
        return str(self.venta) #como va a aparecer en el panel admin


