from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Post, Comentario
from .forms import Formulario_Alta_Post


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


class Alta_post(CreateView):
	model = 'Post'
	form_class = Formulario_Alta_Post
	template_name = 'blog/altaPost.html'
	success_url = reverse_lazy('')

	# def post_nuevo(request):
 	# 	form_class= Formulario_Alta_Post()
    # 	return render(request, 'blog/altaPost.html', {'form': form})

