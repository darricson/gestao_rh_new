from django.db import models
# importado o modulo User para pegarmos a sessão do usuario
from django.contrib.auth.models import User
from django.urls import reverse
from departamentos.models import Departamento
from empresas.models import Empresa

# Create your models here.


class Funcionario(models.Model):
    nome = models.CharField(max_length=50, help_text='Nome do funcionario')
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT,
                                null=True, blank=True)
    
    # metodo para retorna do banco o caminho da url apos atualizar o funcionario
    def get_absolute_url(self):
        return reverse('list_funcionarios')
    
    def __str__(self):
        return self.nome