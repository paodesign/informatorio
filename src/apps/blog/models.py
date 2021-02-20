from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    id=models.AutoField(primary_key=True)
    #id_user = models.ForeignKey('Usuario',on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField()
    categoria = models.CharField(max_length=100)
        
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    id = models.AutoField(primary_key=True)
    #id_user = models.ForeignKey('Usuario',on_delete=CASCADE)
    id_post = models.ForeignKey('Post',on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField()