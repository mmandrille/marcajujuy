# Generated by Django 2.0.3 on 2018-04-17 21:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hunter', '0006_auto_20180417_1746'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='capturado',
            name='header',
        ),
        migrations.AlterField(
            model_name='capturado',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 17, 18, 8, 9, 218957), verbose_name='Fecha de Acceso'),
        ),
    ]
