from django.contrib import admin

from .models import Archivo, Comentario, Faq, Consulta, Respuesta
# Register your models here.
admin.site.register(Archivo)
admin.site.register(Comentario)
admin.site.register(Faq)
admin.site.register(Consulta)
admin.site.register(Respuesta)