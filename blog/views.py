
# coding: latin-1
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Alzheimer
from django.urls import reverse
from django.contrib import admin
from django.views.generic.base import RedirectView
from .forms import PostForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from account.scripts.upload_volbrain import SegmentationVolbrain
from django.conf import settings
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
    alzheimer = Alzheimer.objects.all().order_by('-id')
    return render(request, 'blog/alzheimer_list.html', {'alzheimer':alzheimer})
def post_detail(request, slug):
    alzheimer = get_object_or_404(Alzheimer, slug=slug)
    return render(request, 'blog/post_detail.html', {'alzheimer':alzheimer})
@login_required
def post_create(request):
    form = PostForm()
    retorno=0
    if(request.method == 'POST'):
        form = PostForm(request.POST, request.FILES)
        user = request.user
        if(form.is_valid()):
            file = request.FILES['imagem']
            filename = file.name
            post_nome = file.name
            post_imagem = form.cleaned_data['imagem']
            post_idade =  int(form.cleaned_data['idade'])
            post_sexo = form.cleaned_data['sexo']
            post_autor = user
            post_status_seg = 1
             #Salva no banco de dados
            new_post = Alzheimer(nome=post_nome, imagem=post_imagem, idade=post_idade,  sexo=post_sexo, autor=post_autor,  status_seg=post_status_seg)
            new_post.save()
            id_post = new_post.id
            print(id_post)
            #Instancia class para início do selenium
            teste = SegmentationVolbrain()
            #Chama função para configuração dop selenium 
            teste.setup_method()
            #Inicia o processo de submissão na página do volbrain 
            retorno = teste.submit_volbrain(settings.BASE_DIR+ settings.MEDIA_URL+filename, post_sexo, post_idade, filename, id_post)
            if retorno==404:
                return render(request, 'blog/novo_pedido.html', {'form':form, 'retorno':retorno})
            else:
                return redirect('blog:alzheimer_list')
    return render(request, 'blog/novo_pedido.html', {'form':form})