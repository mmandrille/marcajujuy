from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.core.mail import EmailMessage
#Import Personales
from .models import Archivo, Comentario, Faq, Consulta, Respuesta
from .forms import ComentarioForm, BuscarForm, ContactoForm, ResponderForm

#@login_required
def home(request):
    #Obtenemos los archivos que se van a mostrar:
    archivos = Archivo.objects.order_by('pub_date')[:5]
    #Analizamos si nos mandaron una consulta
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            #Procesamos el mensaje
            consulta = Consulta()
            consulta.email = form.cleaned_data['email']
            consulta.nombre = form.cleaned_data['nombre']
            consulta.mensaje = form.cleaned_data['mensaje']
            consulta.save()
    form = ContactoForm()
    #Obtenemos los datos del FAQ
    faqs = Faq.objects.all()
    #Enviamos la pagina
    return render(request, 'home.html', {'faqs' : faqs, 'archivos': archivos, 'form' : form })
    
def mostrar_listado(request):
    if request.method == 'POST':
        form = BuscarForm(request.POST)
        if form.is_valid():
            archivos = Archivo.objects.filter(nombre__icontains=form.cleaned_data['texto'])
    else:
        archivos = Archivo.objects.order_by('pub_date')[:5]
    form = BuscarForm
    return render(request, 'listado_archivos.html', {'archivos': archivos, 'form' : form})

def mostrar_archivo(request, archivo_id):
    #Si deja un comentario
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = Comentario()
            comentario.archivo = Archivo.objects.get(pk=archivo_id)
            comentario.usuario = request.user
            comentario.comentario = form.cleaned_data['comentario']
            comentario.save()
    #Intentamos cargar el Archivo
    try:
        archivo = Archivo.objects.get(pk=archivo_id)
        #Obtenemos todos los comentarios
        comentarios = Comentario.objects.filter(archivo=archivo_id)

        #Formulario de Comentario
        form = ComentarioForm()
    except Archivo.DoesNotExist:
        raise Http404("El Archivo No Existe")
    #Si salio bien mostramos el archivo
    return render(request, 'mostrar_archivo.html', {'archivo': archivo, 'comentarios': comentarios, 'form': form})

@staff_member_required
def mostrar_consultas(request):
    consultas = Consulta.objects.all()
    return render(request, 'consultas.html', {'consultas' : consultas })

@staff_member_required
def responder_consulta(request, consulta_id):
    #Obtenemos la Consulta Especifica
    consulta = Consulta.objects.get(id=consulta_id)
    #Si se respondio a la misma:
    if request.method == 'POST':
        form = ResponderForm(request.POST)
        if form.is_valid():
            respuesta = Respuesta()
            respuesta.consulta = consulta
            respuesta.usuario = User.objects.get(username=request.user.username)
            respuesta.respuesta = form.cleaned_data['respuesta']
            respuesta.save()
            consulta.respondida = True
            consulta.save()
            #Enviar Correo
            mensaje = 'Su consulta fue: ' + consulta.mensaje + '\n' + 'Nuestra Respuesta:' + respuesta.respuesta
            email = EmailMessage('Marca Jujuy - Respuesta a Su consulta.',
                       mensaje, to=[consulta.email])
            email.send()
    #Instanciamos Formulario de Respuesta
    form = ResponderForm()
    return render(request, 'responder.html', {'consulta' : consulta, 'form' : form, })