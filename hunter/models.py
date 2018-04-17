from __future__ import unicode_literals
import datetime

from django.db import models

class Link(models.Model):
    nombre = models.TextField(max_length=50, null=True)
    objetivo = models.TextField(max_length=50, null=True)
    link_destino = models.URLField()

class Capturado(models.Model):
    models.ForeignKey(Link, on_delete=models.CASCADE)
    datetime = models.DateTimeField('Fecha de Acceso', default=datetime.datetime.now())
    request = models.TextField(null=True)
    ip = models.TextField(null=True)
    ip_extra = models.TextField(null=True)
    is_ruteable = models.BooleanField(default=True)