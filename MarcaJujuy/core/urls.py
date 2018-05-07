from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'corejujuy'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url('^archivo/$', views.mostrar_listado, name='mostrar_listado'),
    path('archivo/<int:archivo_id>/', views.mostrar_archivo, name='mostrar_archivo'),

    url('^consultas/$', views.mostrar_consultas, name='mostrar_consultas'),
    path('responder/<int:consulta_id>/', views.responder_consulta, name='responder_consulta'),
]