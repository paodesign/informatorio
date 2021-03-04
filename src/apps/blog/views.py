from django.shortcuts import render, redirect
from django.views.generic import *
from django.urls import reverse_lazy, reverse
from .models import Post, Comentario
from .forms import Formulario_Alta_Post
from django.http import HttpResponse, HttpResponseRedirect


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

class Editar_post(UpdateView):
	model = Post
	form_class = Formulario_Alta_Post
	template_name='blog/altaPost.html'
	success_url=reverse_lazy('home')


# class Eliminar_post(DeleteView):
# 	model=Post
# 	form_class = Formulario_Alta_Post
# 	template_name='blog/bajaPost.html'
# 	success_url=reverse_lazy('home')

def eliminar_post(request, pk):
	post = Post.objects.get(id=pk)
	post.delete()
	return HttpResponseRedirect('/')
	
class Alta_post(CreateView):
	model = Post 
	form_class = Formulario_Alta_Post
	template_name = 'blog/altaPost.html'
	success_url = reverse_lazy('home')

# No hace falta, se esta usando la clase
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

