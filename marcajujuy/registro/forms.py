from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    localidad = forms.CharField(max_length=30)
    telefono = forms.CharField(max_length=20)
    empresa = forms.CharField(max_length=100)
    producto = forms.CharField(widget=forms.widgets.Textarea())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
