from django.urls import path
from django.contrib import admin
from . import views
app_name = 'blog'


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('sobre-nos/', views.about, name='about'),
    path('<slug:slug>', views.post_detail, name='post_detail'),
    path('novo_pedido/', views.post_create, name='novo_pedido'),
    path('alzheimer_list/', views.alzheimer_list, name='alzheimer_list'),
    path('accounts/profile/', views.alzheimer_list, name='alzheimer_list'),
    #path('account/logout/', views.post_list, name='post_list'),
]