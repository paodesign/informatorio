
from django.urls import path
from . import views

urlpatterns = [
  path('', views.listar),
  path('listar/', views.listar, name = 'listar_blog')
]