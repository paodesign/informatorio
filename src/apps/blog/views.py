from django.shortcuts import render, redirect
from django.views.generic import *

from django.urls import reverse_lazy
from .models import Post, Comentario

from django.urls import reverse_lazy, reverse
from .models import Post, Comentario, Categoria

from .forms import Formulario_Alta_Post
from .forms import Formulario_Alta_Comentario
from django.http import HttpResponse


#Creacion de las vistas

class Home(ListView):
	model = Post
	template_name = 'blog/home.html'


#utilice una funcion para definir esta vista porque se necesita utilizar los dos modelos

def post(request, pk):
	post = Post.objects.get(id=pk)
	comentarios = Comentario.objects.filter(post= post.id)
	
	###ESTA PARTE ES DEL FORMULARIO PARA EL COMENTARIO####
	if request.method == 'POST':
		form = Formulario_Alta_Comentario(request.POST)
		if form.is_valid():
			comentario = form.save(commit=False)
			comentario.post = post
			comentario.save()


			#return redirect('home') ### Te devuelve a la home despues de comentar, me parece que no sirve 
			#por eso lo anulo
	else:
		form = Formulario_Alta_Comentario()
	###########  ACA TERMINA LO DEL FORMULARIO PARA EL COMENTARIO     ##########	
	ctx = {'post':post, 'comentarios': comentarios, 'form' : form}
	return render(request, 'blog/post.html', ctx)








class Editar_post(UpdateView):
	model = Post
	form_class = Formulario_Alta_Post
	template_name='blog/altaPost.html'
	success_url=reverse_lazy('home')

class Eliminar_post(DeleteView):
	model=Post
	success_url=reverse_lazy('home')
	
class Alta_post(CreateView):
	model = Post 
	form_class = Formulario_Alta_Post
	template_name = 'blog/altaPost.html'
	success_url = reverse_lazy('home')

def vista_categorias(request, categ):
	categoria_posts = Post.objects.filter(categoria=categ)
	existe = Categoria.objects.filter(categoria_nombre=categ)
	return render(request, 'blog/categorias.html', {'categ':categ.title(), 'categoria_posts':categoria_posts, 'existe':existe})





# No hace falta, se esta usando la clase "Alta_post"
#def post_nuevo(request):
#	if request.method == 'POST':
#		form = Formulario_Alta_Post(request.POST)
#		if form.is_valid():
#			form.save()
#			return redirect('home')
#	else:
#		
#		form = Formulario_Alta_Post()
#
#	ctx = {'form' : form}
#	return render(request, 'blog/altaPost.html', ctx)

	# else:
	# 	form = Formulario_Alta_Post(request.POST)
	# 	ctx= {'form' : form}
	# 	if form.is_valid():
	# 		form.save()
	# 		return redirect('home')

