from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name="index"),
    path('internacional/', internacional, name="internacional"),
    path('deportes/', deportes, name="deportes"),
    path('formulario/', formulario, name="formulario"),
    path('login/', login, name="login"),
    path('nacional/', nacional, name="nacional"),
    path('registro/', registro, name="registro"),
    path('datosutil/', datoSutil, name="datosSutil"),
    path('reportajes/', reportajes, name="Reportajes"),
    path('salud/', salud, name="Salud"),
    path('tendencias/', tendencias, name="tendencias"),
    path('entrevistas/', entrevistas, name="entrevistas")
]