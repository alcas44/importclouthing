# Generated by Django 4.0.2 on 2022-06-26 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IngresosApp', '0011_envios_guia'),
    ]

    operations = [
        migrations.AddField(
            model_name='envios',
            name='observacion',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
