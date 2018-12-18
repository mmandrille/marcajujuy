# Generated by Django 2.0.5 on 2018-06-01 19:22

import datetime
from django.conf import settings
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Archivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='Titulo')),
                ('descripcion', tinymce.models.HTMLField()),
                ('captura', models.ImageField(null=True, storage=django.core.files.storage.FileSystemStorage(location='archivos/'), upload_to='')),
                ('archivo', models.FileField(upload_to='')),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2018, 6, 1, 16, 22, 54, 551282), verbose_name='Fecha de Publicacion')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField()),
                ('archivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Archivo')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('nombre', models.CharField(max_length=20, verbose_name='Titulo')),
                ('mensaje', models.TextField()),
                ('respondida', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orden', models.IntegerField()),
                ('pregunta', models.CharField(max_length=200, verbose_name='Titulo')),
                ('respuesta', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta', models.TextField()),
                ('consulta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Consulta')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
