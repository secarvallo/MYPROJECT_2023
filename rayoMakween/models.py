from django.db import models 
import datetime
from distutils.command.upload import upload
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
#---------------------------------------------------------------------------------->
#---------------------------------------------------------------------------------->
class Formulario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    celular = models.IntegerField()
    servicios = models.CharField(max_length=50)
    comentario = models.TextField(max_length=100)

    def __str__(self):
        text = "{0} ({1})"
        return text.format(self.nombre, self.apellido) 
    
#---------------------------------------------------------------------------------->
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id Categoria')
    nombreCategoria = models.CharField(max_length=50, blank=True, verbose_name='Nombre Categoria')

    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
	codigo= models.CharField(primary_key = True, max_length= 8, verbose_name='Codigo')
	marca= models.CharField(max_length=50, verbose_name='Marca')
	modelo= models.CharField(max_length=50, verbose_name= 'Producto')
	#imagen= models.ImageField(upload_to='imagenes', null= True, blank= True, verbose_name='Imagen')
	categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoria')
	precio=models.IntegerField(blank=True, null=True, verbose_name='Precio')

	def __str__(self):
		return self.codigo

class Boleta(models.Model):
      id_boleta=models.AutoField(primary_key=True)
      total= models.BigIntegerField()
      fechaCompra= models.DateTimeField(blank=False, null=False, default = datetime.datetime.now)

      def __str__(self):
        return str(self.id_boleta)
      
class Detalle_boleta(models.Model):
     id_boleta= models.ForeignKey('Boleta', blank=True, on_delete=models.CASCADE)
     id_detalle_boleta= models.AutoField(primary_key=True)
     id_producto= models.ForeignKey('Producto', on_delete=models.CASCADE)
     cantidad= models.IntegerField()
     subtotal= models.BigIntegerField()

     def __str__(self):
          return str(self.id_detalle_boleta)