# Generated by Django 3.2.9 on 2022-07-18 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PagoEfectivo',
            fields=[
                ('venta', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nit', models.CharField(max_length=14)),
                ('fecha', models.CharField(max_length=25)),
                ('total_venta', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tipo_pago', models.CharField(max_length=75)),
                ('total_pago', models.DecimalField(decimal_places=2, max_digits=10)),
                ('verificador', models.IntegerField()),
                ('usuario', models.CharField(max_length=200)),
                ('fecha_sistema', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'pagoefectivo',
                'verbose_name_plural': 'pagoefectivos',
            },
        ),
    ]
