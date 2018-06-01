from django.shortcuts import render

#Import Personales
from .models import Archivo, Comentario
from .forms import ComentarioForm, BuscarForm

# Create your views here.
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
