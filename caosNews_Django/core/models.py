from django.db import models

# Create your models here.

class Usuario(models.Model):
    idUsuario = models.IntegerField(primary_key=True, verbose_name="Id de usuario")
    nombreUsuario = models.CharField(max_length=50, verbose_name="Nombre de usuario")
    apellidoUsuario = models.CharField(max_length=50, verbose_name="Nombre de usuario")
    contraseñaUsuario = models.CharField(max_length=20, verbose_name="Contraseña de usuario")

    def __str__(self):
        return self.nombreUsuario


class Periodista(models.Model):
    runPeriodista = models.CharField(primary_key=True ,max_length=10, verbose_name="run de periodista")
    nombrePeriodista = models.CharField(max_length=30, verbose_name="nombre de periodista")
    apellidoPeriodista = models.CharField(max_length=30, verbose_name="apellido de periodista")
    sueldo = models.IntegerField(verbose_name="sueldo de periodista")
    fechaContrato = models.DateField()
    fechaNacimientoPeriodista = models.DateField()

    def __str__(self):
        return self.nombrePeriodista    

class categoriaNoticia(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="Id de la categoría de la notica")
    nombreCategoria = models.CharField(max_length=25, verbose_name="nombre de la categoría")

    def __str__(self):
        return self.nombreCategoria
    
class Noticia(models.Model):
    idNoticia = models.IntegerField(primary_key=True, verbose_name="Id de la noticia")
    tituloNoticia = models.CharField(max_length=50, verbose_name="titulo de la noticia")
    epigrafe = models.CharField(max_length=100, verbose_name="epígrafe de la noticia")
    cuerpo = models.CharField(max_length=500, verbose_name="Cuerpo de la noticia")
    fotoNoticia = models.BinaryField(null=True)
    periodista = models.ForeignKey(Periodista, on_delete=models.CASCADE)
    categoria = models.ForeignKey(categoriaNoticia, on_delete=models.CASCADE)

    def __str__(self):
        return self.tituloNoticia