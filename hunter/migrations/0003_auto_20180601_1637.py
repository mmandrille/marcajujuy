# Generated by Django 2.0.5 on 2018-06-01 19:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hunter', '0002_auto_20180601_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capturado',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 1, 16, 37, 55, 59069), verbose_name='Fecha de Acceso'),
        ),
    ]
