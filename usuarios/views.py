from django.shortcuts import render
from .models import Usuario

def usuariolist(request):
    get_usuarios = Usuario.objects.all()


    data = {
        'get_usuarios': get_usuarios
    }
    return render(request, 'usuariolist.html', data)