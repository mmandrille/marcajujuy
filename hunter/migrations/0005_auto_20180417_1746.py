# Generated by Django 2.0.3 on 2018-04-17 20:46

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hunter', '0004_auto_20180417_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='capturado',
            name='link',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hunter.Link'),
        ),
        migrations.AddField(
            model_name='capturado',
            name='meta',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='capturado',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 17, 17, 46, 19, 53969), verbose_name='Fecha de Acceso'),
        ),
    ]