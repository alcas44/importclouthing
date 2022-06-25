from django.db import models


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
