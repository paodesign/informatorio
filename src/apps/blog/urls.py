
from django.urls import path
from . import views
from . views import Home, post


urlpatterns = [
  path('', Home.as_view(), name = 'home'),
  path('posts/<int:pk>', post , name = 'posts'),
]