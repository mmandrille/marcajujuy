from django.contrib import admin

from .models import Faq, Consulta, Respuesta
# Register your models here.
admin.site.register(Faq)
admin.site.register(Consulta)
admin.site.register(Respuesta)