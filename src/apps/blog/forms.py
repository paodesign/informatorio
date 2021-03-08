from django import forms
from .models import Post, Comentario
from django.contrib.auth.forms import UserCreationForm
from ..usuario.models import Usuario
# from .forms import Formulario_Post

class Formulario_Alta_Post(forms.ModelForm):

    class Meta:
        model = Post
        #fields = ('titulo', 'contenido', 'id_user', 'categoria')
        fields='__all__'
        widgets = {
        	'titulo': forms.TextInput(attrs={'class': 'form-control'}),
        	'id_user': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'identificador', 'type':'hidden'}),
        	'contenido': forms.Textarea(attrs={'class': 'form-control'}),
           'categoria': forms.Select(attrs={'class': 'form-control'}),
        }

class Formulario_Alta_Comentario(forms.ModelForm):
  class Meta:
    model = Comentario
    fields = ('contenido', 'autor')

    widgets = {
    #'titulo': forms.TextInput(attrs={'class': 'form-control'}),
   'autor': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'identificador', 'type':'hidden'}),
  'contenido': forms.Textarea(attrs={'class': 'form-control'}),
      #'categoria': forms.Select(attrs={'class': 'form-control'}),



    }
          
        







#class Formulario_Registro_Usuario(UserCreationForm):
 #   class Meta:
  #      model = Usuario
   #     fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
		