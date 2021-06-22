from django.shortcuts import render

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
    return render(request, 'core/Registro.html')
