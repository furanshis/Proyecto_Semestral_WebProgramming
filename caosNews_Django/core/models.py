from django.db import models

# Create your models here.

class Usuario(models.Model):
    idUsuario = models.IntegerField(primary_key=True, verbose_name="Id de usuario")
    nombreUsuario = models.CharField(max_length=50, verbose_name="Nombre de usuario")
    apellidoUsuario = models.CharField(max_length=50, verbose_name="Nombre de usuario")
    contraseñaUsuario = models.CharField(max_length=20, verbose_name="Contraseña de usuario")

    def __str__(self):
        return self.nombreUsuario

class Noticia(models.Model):
    idNoticia = models.IntegerField(primary_key=True, verbose_name="Id de la noticia")
    tituloNoticia = models.CharField(max_length=50, verbose_name="titulo de la noticia")
    epigrafe = models.CharField(max_length=100, verbose_name="epígrafe de la noticia")
    cuerpo = models.CharField(max_length=500, verbose_name="Cuerpo de la noticia")
    fotoNoticia = models.BinaryField(null=True)