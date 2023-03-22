from django.db import models
from django.contrib.auth.models import User
from departamentos.models import Departamento
from empresas.models import Empresa

# Create your models here.


class Funcionario(models.Model):
    name = models.CharField(max_length=50, help_text='Nome do funcionario')
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name