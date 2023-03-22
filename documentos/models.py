from django.db import models
from funcionarios.models import Funcionario

# Create your models here.


class Documento(models.Model):
    description = models.CharField(max_length=100, help_text='Descrição')
    pertence = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    
    
    def __str__(self):
        return self.description