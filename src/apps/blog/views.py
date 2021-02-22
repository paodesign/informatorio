from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.
from django.shortcuts import render
from .models import post

class Home(ListView):
	model = post
	template_name = 'blog/home.html'

#def home(request):
   # return render(request, 'blog/home.html')

#def post(request):
    #return render(request,'blog/post.html')


class Detallepost(DetailView):
	model = post
	template_name = 'blog/post.html'