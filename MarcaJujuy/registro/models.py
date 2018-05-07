from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    nombre = models.TextField(max_length=50, null=True)
    apellido = models.TextField(max_length=50, null=True)
    localidad = models.CharField(max_length=30, blank=True)
    telefono = models.TextField(max_length=20,null=True)
    empresa = models.TextField(max_length=100, null=True)
    producto = models.TextField(null=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
