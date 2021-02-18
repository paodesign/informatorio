from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def listar(request):
    return render(request,'blog/listar.html')