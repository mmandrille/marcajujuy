import datetime
from django.shortcuts import redirect
from ipware import get_client_ip
#Modelos creados
from .models import Link, Capturado
# Create your views here.
def hunt_usuario(request, link_id):
    "Obtenemos el link trampa"
    l = Link.objects.get(pk=link_id)
    "Aqui debemos guardar la informacion obtenida"
    c = Capturado()
    c.datetime = datetime.datetime.now()
    c.ip, c.is_ruteable = get_client_ip(request)
    c.request =  '\n'.join('{}: {}'.format(k, v)
                          for k, v in request.META.items()
                          if k.startswith('HTTP_'))
    c.save()
    "Lo enviamos al link destino elegido sin que se entere que lo trackeamos>"
    return redirect(l.link_destino)