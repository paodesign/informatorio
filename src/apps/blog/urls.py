
from django.urls import path
from . import views
from . views import Home, post, Alta_post, post_nuevo

urlpatterns = [
  path('', Home.as_view(), name = 'home'),
  path('home/', Home.as_view(), name = 'home'),
  path('posts/<int:pk>', post , name = 'posts'),
  path('crear/', views.Alta_post.as_view(), name = 'alta_post'),
  path('nuevo/', post_nuevo, name = 'nuevo'),
]