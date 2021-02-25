from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Post, Comentario

#Creacion de las vistas

class Home(ListView):
	model = Post
	template_name = 'blog/home.html'

#utilice una funcion para definir esta vista porque se necesita utilizar los dos modelos

def post(request, pk):
	post = Post.objects.get(id=pk)
	comentarios = Comentario.objects.filter(post= post.id)
	ctx = {'post':post, 'comentarios': comentarios}
	return render(request,'blog/post.html',ctx)


