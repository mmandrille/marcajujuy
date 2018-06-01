from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'biblioteca'
urlpatterns = [
    url('^$', views.mostrar_listado, name='mostrar_listado'),
    path('<int:archivo_id>/', views.mostrar_archivo, name='mostrar_archivo'),
]