from django import forms
from .models import Post, Comentario
# from .forms import Formulario_Post

class Formulario_Alta_Post(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

