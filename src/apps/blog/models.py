from django.db import models
from django.utils import timezone
from datetime import datetime


# Creacion de modelos
class Post(models.Model):
    id=models.AutoField(primary_key=True)
    #id_user = models.ForeignKey('Usuario',on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    #hora = models.TimeField(blank = True,null=True)
    categoria = models.ForeignKey('Categoria', to_field='categoria_nombre', on_delete = models.SET_NULL, null=True)
    imagen = models.ImageField(upload_to = 'post', blank = True)


        
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    id = models.AutoField(primary_key=True)
    #id_user = models.ForeignKey('Usuario',on_delete=CASCADE)
    
    post = models.ForeignKey('Post', on_delete=models.CASCADE, )
    contenido = models.TextField()
    #fecha_creacion = models.DateTimeField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)



    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.contenido

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    categoria_nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.categoria_nombre


    

# class Generador_post(models.Model):
#     titulo = models.CharField(max_length = 100)
#     contenido = models.TextField()
#     fecha_creacion = models.DataTimeField()
