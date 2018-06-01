from django.contrib import admin

#Incluimos modelos
from .models import Album, Foto

#Definimos inline
class FotoInline(admin.TabularInline):
    model = Foto

class AlbumAdmin(admin.ModelAdmin):
    inlines = [
        FotoInline,
    ]

# Register your models here.
admin.site.register(Album, AlbumAdmin)