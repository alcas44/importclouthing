# Generated by Django 4.0.2 on 2022-06-26 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IngresosApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='envios',
            name='venta',
            field=models.CharField(default=' ', max_length=100),
            preserve_default=False,
        ),
    ]
