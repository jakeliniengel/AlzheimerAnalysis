from django.contrib import admin
from .models import  Alzheimer, Segmentation

# Register your models here.

class AlzheimerAdmin(admin.ModelAdmin):
    list_display =('imagem', 'idade', 'autor', 'created_at', 'sexo')
    search_fields=['nome']

admin.site.register(Alzheimer, AlzheimerAdmin)
admin.site.register(Segmentation)
