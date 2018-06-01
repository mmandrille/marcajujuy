from django.conf.urls import url
from django.urls import path
#Import personales
from . import views

app_name = 'fotos'
urlpatterns = [
    path('', views.fotos, name='fotos'),
    path('<int:album_id>/', views.album, name='album'),
]