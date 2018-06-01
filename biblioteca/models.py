from __future__ import unicode_literals
import datetime

from django.db import models
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import *
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation

#Import Modulos Extra
from star_ratings.models import Rating
from tinymce.models import HTMLField

#Import Personales
from marcajujuy.settings import MEDIA_URL

#Create your models here.
class Archivo(models.Model):
    nombre = models.CharField('Titulo', max_length=200)
    descripcion = HTMLField()
    captura = models.ImageField(storage=FileSystemStorage(location=MEDIA_URL), null=True)
    archivo = models.FileField(upload_to='')
    pub_date = models.DateTimeField('Fecha de Publicacion', default=datetime.datetime.now())
    ratings = GenericRelation(Rating, related_query_name='archivos')
    def __str__(self):
        return self.nombre

#Comentarios
class Comentario(models.Model):
    archivo = models.ForeignKey(Archivo, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Usuario')
    comentario = models.TextField()
    def __str__(self):
        return self.archivo.nombre + '-' + self.usuario.username