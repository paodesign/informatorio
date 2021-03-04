from django import forms
from .models import Post, Comentario
# from .forms import Formulario_Post

class Formulario_Alta_Post(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

class Formulario_Alta_Comentario(forms.ModelForm):
	class Meta:
		model = Comentario
		fields = ['contenido']
		