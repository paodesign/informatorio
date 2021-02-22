
from django.urls import path
from . import views
from .views import Home, Detallepost


urlpatterns = [
  #path('', views.home, name = 'home'),
  path('', Home.as_view(), name='home'),
  path('post/<int:pk>', Detallepost.as_view(), name = 'post')
]