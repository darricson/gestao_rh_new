from django.db import models
from django.urls import reverse
from empresas.models import Empresa

# Create your models here.


class Departamento(models.Model):
    name = models.CharField(max_length=70, help_text='Departamento')
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    
    def get_absolute_url(self):
        return reverse('list_departamentos')
    
    def __str__(self):
        return self.name