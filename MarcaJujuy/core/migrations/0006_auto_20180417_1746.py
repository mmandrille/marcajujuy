# Generated by Django 2.0.3 on 2018-04-17 20:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20180417_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivo',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 17, 17, 46, 19, 46396), verbose_name='Fecha de Publicacion'),
        ),
    ]
