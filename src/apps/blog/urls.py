
from django.urls import path
from . import views
from . views import Home, post, Alta_post

urlpatterns = [
  path('', Home.as_view(), name = 'home'),
  path('posts/<int:pk>', post , name = 'posts'),
  path('home/nuevo/', views.Alta_post.as_view(), name = 'alta_post'),
]