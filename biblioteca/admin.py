from django.contrib import admin

from .models import Archivo, Comentario
# Register your models here.
admin.site.register(Archivo)
admin.site.register(Comentario)