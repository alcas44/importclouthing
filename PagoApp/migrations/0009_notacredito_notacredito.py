# Generated by Django 4.0.2 on 2022-07-20 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PagoApp', '0008_notacredito'),
    ]

    operations = [
        migrations.AddField(
            model_name='notacredito',
            name='notacredito',
            field=models.CharField(default=' ', max_length=35),
            preserve_default=False,
        ),
    ]