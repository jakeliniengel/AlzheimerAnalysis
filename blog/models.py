from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Alzheimer(models.Model):
    SEXO=(
        ('Female', 'Feminino'),
        ('Male', 'Masculino')
    )
    STATUS=(
        ('0', 'Erro'),
        ('1', 'Processando'),
        ('2', 'Consluído'),
    )
    nome =models.CharField(max_length=200)
    imagem = models.FileField()
    slug = models.SlugField()
    idade = models.DecimalField(max_digits=6, decimal_places=0)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    sexo = models.CharField(max_length=15, choices=SEXO)
    status_seg = models.CharField(max_length=20, choices=STATUS, default='1')


class Segmentation(models.Model):
    paciente = models.ForeignKey(Alzheimer, on_delete=models.CASCADE)
    ca1_right = models.DecimalField(max_digits=10, decimal_places=6)
    ca1_left = models.DecimalField(max_digits=10, decimal_places=6)
    ca2_ca3_right = models.DecimalField(max_digits=10, decimal_places=6)
    ca2_ca3_left = models.DecimalField(max_digits=10, decimal_places=6)
    subic_right = models.DecimalField(max_digits=10, decimal_places=6)
    subic_left = models.DecimalField(max_digits=10, decimal_places=6)