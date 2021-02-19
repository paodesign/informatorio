from django.db import models
from django.utils import timezone

# Create your models here.
class Autor(models.Model):
    identificador = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre



class Post(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_publicacion = models.DateTimeField()
    categoria = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT)

    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
	    return self.titulo




