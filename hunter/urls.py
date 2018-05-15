from django.urls import path
#Import Personales
from . import views

urlpatterns = [
    path('h/<int:link_id>/', views.hunt_usuario, name='hunt_usuario'),
]