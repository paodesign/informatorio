
from django.shortcuts import render

def principal(request):

    return render(request, 'prueba.html')

def segunda(request):

    return render(request, 'segundo.html')