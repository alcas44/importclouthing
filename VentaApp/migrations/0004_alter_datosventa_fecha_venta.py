# Generated by Django 3.2.9 on 2022-07-01 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VentaApp', '0003_alter_datosventa_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datosventa',
            name='fecha_venta',
            field=models.CharField(max_length=20),
        ),
    ]
