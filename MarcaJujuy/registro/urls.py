from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path
#Import Personales
from . import views

urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^administracion/$', views.administracion, name='administracion'),
    url(r'^usuarios/$', views.mostrar_usuarios, name='mostrar_usuarios'),
    path('activar/<int:user_id>/', views.activar_usuario, name='activar_usuario'),
    path('desactivar/<int:user_id>/', views.desactivar_usuario, name='desactivar_usuario'),
]
