from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'blog/home.html')

def post(request):
    return render(request,'blog/post.html')