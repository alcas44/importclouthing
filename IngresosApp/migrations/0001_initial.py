# Generated by Django 4.0.2 on 2022-06-26 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=75)),
                ('referencia', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=200)),
                ('marca', models.CharField(max_length=200)),
                ('precio_compra', models.FloatField()),
                ('precio_venta', models.FloatField()),
                ('descuento', models.FloatField(null=True)),
                ('existencia', models.IntegerField(default=0)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='articulos')),
                ('usuario', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'articulo',
                'verbose_name_plural': 'articulos',
            },
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=75)),
                ('nit', models.CharField(max_length=14)),
                ('tipo', models.CharField(max_length=50)),
                ('nombres', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=500)),
                ('telefono', models.CharField(max_length=9)),
                ('correo', models.CharField(blank=True, max_length=250)),
                ('fecha_nac', models.DateField(blank=True)),
                ('cuenta', models.FloatField()),
                ('usuario', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'cliente',
                'verbose_name_plural': 'clientes',
            },
        ),
        migrations.CreateModel(
            name='Envios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=75)),
                ('tipo', models.CharField(max_length=200)),
                ('remitente', models.CharField(max_length=200)),
                ('destinatario', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=500)),
                ('telefono', models.CharField(max_length=9)),
                ('estado', models.CharField(max_length=75)),
                ('monto', models.FloatField(blank=True)),
                ('guia', models.CharField(blank=True, max_length=100)),
                ('observacion', models.CharField(blank=True, max_length=500)),
                ('usuario', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'envios',
                'verbose_name_plural': 'envios',
            },
        ),
    ]
