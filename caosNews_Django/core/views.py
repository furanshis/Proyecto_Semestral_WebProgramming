from django.shortcuts import render
from .models import Noticia

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def internacional(request):
    return render(request, 'core/internacional.html')

def deportes(request):
    return render(request, 'core/deportes.html')

def formulario(request):
    return render(request, 'core/Formulario.html')

def login(request):
    return render(request, 'core/login.html')

def nacional(request):
    return render(request, 'core/Nacional.html')

def registro(request):
    return render(request, 'core/registro2.html')

def datoSutil(request):
    return render(request, 'core/datosutil.html')

def reportajes(request):
    return render(request, 'core/reportajes.html')

def salud(request):
    return render(request, 'core/salud.html')

def tendencias(request):
    return render(request, 'core/tendencias.html')

def entrevistas(request):
    return render(request, 'core/entrevistas.html')


def listarNoticias(request):

    noticias = Noticia.object.all()

    datos = {
        'datos': noticias
    }


    return render(request, 'core/listarNoticias.html', datos)
