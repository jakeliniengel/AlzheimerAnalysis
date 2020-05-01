from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Alzheimer
from django.urls import reverse
from django.contrib import admin
from django.views.generic.base import RedirectView
from .forms import PostForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

#from django.forms import UploadFileForm

# Imaginary function to handle an uploaded file.
#from somewhere import handle_uploaded_file

# Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html')
def about(request):
    return render(request, 'blog/about-us.html')
def contact(request):
    return render(request, 'blog/contact.html')
def alzheimer_list(request):
    alzheimer = Alzheimer.objects.all().order_by('-created_at')
    return render(request, 'blog/alzheimer_list.html', {'alzheimer':alzheimer})
def post_detail(request, slug):
    alzheimer = get_object_or_404(Alzheimer, slug=slug)
    return render(request, 'blog/post_detail.html', {'alzheimer':alzheimer})
@login_required
def post_create(request):
    form = PostForm()

    if(request.method == 'POST'):
        form = PostForm(request.POST, request.FILES)
        if(form.is_valid()):
            post_nome = form.cleaned_data['nome']
            post_imagem = form.cleaned_data['imagem']
            #post_slug = form.cleaned_data['slug']
            post_idade = form.cleaned_data['idade']
            post_sexo = form.cleaned_data['sexo']
            post_autor = form.cleaned_data['autor']
            new_post = Alzheimer(nome=post_nome, imagem=post_imagem, idade=post_idade,  sexo=post_sexo, autor=post_autor)
            new_post.save()
            return redirect('blog:alzheimer_list')
    return render(request, 'blog/novo_pedido.html', {'form':form})