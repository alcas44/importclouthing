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







class PagoCheque(models.Model):
    venta = models.BigIntegerField(primary_key=True,null=False)
    nit = models.CharField(max_length=14,blank=False,null=False)
    fecha = models.CharField(max_length=25,blank=False,null=False)
    numero_cheque = models.IntegerField(blank=False,null=False)
    banco = models.CharField(max_length=250,blank=False,null=False)
    fecha_cheque = models.CharField(max_length=25,blank=False,null=False)
    total_venta = models.DecimalField(max_digits=10,decimal_places=2,blank=False)
    monto = models.DecimalField(max_digits=10,decimal_places=2,blank=False)
    tipo_pago = models.CharField(max_length=75,blank=False,null=False)
    abono = models.DecimalField(max_digits=10,decimal_places=2,blank=False,null=False)
    verificador = models.IntegerField()
    estado = models.IntegerField(blank=False,null=False)
    usuario = models.CharField(max_length=200,blank=False)
    fecha_sistema = models.DateTimeField(blank=False,null=False)

    class Meta:#nombre que tendran en singular y plural
        verbose_name="pagocheque"
        verbose_name_plural="pagocheques"

    def __str__(self):
        return str(self.venta) #como va a aparecer en el panel admin






class PagoTarjeta(models.Model):
    venta = models.BigIntegerField(primary_key=True,null=False)
    nit = models.CharField(max_length=14,blank=False,null=False)
    fecha = models.CharField(max_length=25,blank=False,null=False)
    tipo_tarjeta = models.CharField(max_length=75,blank=False,null=False)
    tipo_pago = models.CharField(max_length=75,blank=False,null=False)
    numero_tarjeta = models.CharField(max_length=16,blank=False,null=False)
    banco = models.CharField(max_length=250,blank=False,null=False)
    autorizacion = models.CharField(max_length=25,blank=False,null=False)
    total_venta = models.DecimalField(max_digits=10,decimal_places=2,blank=False)
    verificador = models.IntegerField()
    observaciones = models.CharField(max_length=250,blank=False)
    estado = models.IntegerField(blank=False,null=False)
    usuario = models.CharField(max_length=200,blank=False)
    fecha_sistema = models.DateTimeField(blank=False,null=False)

    class Meta:#nombre que tendran en singular y plural
        verbose_name="pagotarjeta"
        verbose_name_plural="pagotarjetas"

    def __str__(self):
        return str(self.venta) #como va a aparecer en el panel admin





class PagoDeposito(models.Model):
    venta = models.BigIntegerField(primary_key=True,null=False)
    nit = models.CharField(max_length=14,blank=False,null=False)
    fecha = models.CharField(max_length=25,blank=False,null=False)
    tipo_pago = models.CharField(max_length=75,blank=False,null=False)
    numero_boleta = models.CharField(max_length=16,blank=False,null=False)
    banco = models.CharField(max_length=250,blank=False,null=False)
    monto_deposito = models.DecimalField(max_digits=10,decimal_places=2,blank=False)
    fecha_deposito = models.CharField(max_length=25,blank=False,null=False)
    total_venta = models.DecimalField(max_digits=10,decimal_places=2,blank=False)
    verificador = models.IntegerField()
    observaciones = models.CharField(max_length=250,blank=False)
    estado = models.IntegerField(blank=False,null=False)
    usuario = models.CharField(max_length=200,blank=False)
    fecha_sistema = models.DateTimeField(blank=False,null=False)

    class Meta:#nombre que tendran en singular y plural
        verbose_name="pagotarjeta"
        verbose_name_plural="pagotarjetas"

    def __str__(self):
        return str(self.venta) #como va a aparecer en el panel admin