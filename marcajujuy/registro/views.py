from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.core.mail import EmailMessage
from django.http import HttpResponse, HttpResponseRedirect

#Import personales
from .decorators import anonymous_required
from .forms import SignUpForm

#Vistas
@anonymous_required
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            #Elementos del Perfil
            user.profile.nombre = form.cleaned_data.get('nombre')
            user.profile.apellido = form.cleaned_data.get('apellido')
            user.profile.localidad = form.cleaned_data.get('localidad')
            user.profile.telefono = form.cleaned_data.get('telefono')
            user.profile.empresa = form.cleaned_data.get('empresa')
            user.profile.producto = form.cleaned_data.get('producto')
            #Guardamos el usuario
            user.is_active = False
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            login(request, user)
            return render(request, 'registrado.html',)
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@staff_member_required
def administracion(request):
    return render(request, 'administracion.html',)

@staff_member_required
def mostrar_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'listado_usuarios.html', {'usuarios': usuarios,})

@staff_member_required
def activar_usuario(request, user_id):
    usuario = User.objects.get(id=user_id)
    usuario.is_active = True
    usuario.save()
    #Enviar Correo
    email = EmailMessage('Su cuenta de Marca Jujuy a sido Activada.',
                       'Bienvenido!', to=[usuario.email])
    email.send()
    return render(request, 'activado.html', {'usuario' : usuario})

@staff_member_required
def desactivar_usuario(request, user_id):
    usuario = User.objects.get(id=user_id)
    usuario.is_active = False
    usuario.save()
    return render(request, 'desactivado.html')