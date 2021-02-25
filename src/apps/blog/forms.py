from django import forms
from .models import Producto, Rubro

class Formulario_Alta(forms.ModelForm):

    class Meta:
        
