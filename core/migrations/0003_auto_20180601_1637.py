# Generated by Django 2.0.5 on 2018-06-01 19:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180601_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivo',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 1, 16, 37, 55, 50262), verbose_name='Fecha de Publicacion'),
        ),
    ]
