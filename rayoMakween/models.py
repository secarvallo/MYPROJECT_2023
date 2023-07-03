from django.db import models 

# Create your models here.

class formulario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    celular = models.CharField(max_length=15)
    comuna = models.CharField(max_length=15)
    region = models.CharField(max_length=15)
    servicios = models.CharField(max_length=15)
    comentario = models.TextField()

    def __str__(self):
        text = "{0} ({1})"
        return text.format(self.nombre, self.apellido) 