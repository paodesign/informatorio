from django import forms
from .models import Post, Comentario
from django.contrib.auth.forms import UserCreationForm
from ..usuario.models import Usuario
# from .forms import Formulario_Post

class Formulario_Alta_Post(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

class Formulario_Alta_Comentario(forms.ModelForm):
	class Meta:
		model = Comentario
		fields = ['contenido']



class Formulario_Registro_Usuario(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
		