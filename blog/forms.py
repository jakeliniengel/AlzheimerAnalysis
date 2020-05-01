from django.forms import ModelForm
from .models import Alzheimer

class PostForm(ModelForm):
    class Meta:
        model = Alzheimer
        fields = ['nome', 'imagem', 'idade', 'sexo', 'autor']