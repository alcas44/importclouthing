# Generated by Django 3.2.9 on 2022-07-05 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VentaApp', '0008_auto_20220705_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalle',
            name='nit',
            field=models.CharField(default=' ', max_length=14),
            preserve_default=False,
        ),
    ]
