from __future__ import unicode_literals
import datetime

from django.db import models
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import *
from django.contrib.auth.models import User
from marcajujuy.settings import MEDIA_URL
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating
from tinymce.models import HTMLField

#Create your models here.
class Archivo(models.Model):
    nombre = models.CharField('Titulo', max_length=200)
    descripcion = models.TextField()
    captura = models.ImageField(storage=FileSystemStorage(location=MEDIA_URL), null=True)
    archivo = models.FileField(upload_to='')
    pub_date = models.DateTimeField('Fecha de Publicacion', default=datetime.datetime.now())
    ratings = GenericRelation(Rating, related_query_name='archivos')
    def __str__(self):
        return self.nombre

#Comentarios
class Comentario(models.Model):
    archivo = models.ForeignKey(Archivo, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    def __str__(self):
        return self.archivo.nombre + '-' + self.usuario.username

#Elementos del FAQ
class Faq(models.Model):
    orden = models.IntegerField()
    pregunta = models.CharField('Titulo', max_length=200)
    respuesta = HTMLField()
    def __str__(self):
        return self.pregunta

#Consulta
class Consulta(models.Model):
    email = models.EmailField()
    nombre = models.CharField('Titulo', max_length=20)
    mensaje = models.TextField()
    respondida = models.BooleanField(default=False)
    def __str__(self):
        return self.email + '-' + self.mensaje

#Respuestas
class Respuesta(models.Model):
    consulta = models.ForeignKey(Consulta, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    respuesta = models.TextField()
    def __str__(self):
        return self.usuario.username + '-' + self.respuesta