from django.db import models
from funcionarios.models import Funcionario
# Create your models here.


class RegistroHoraExtra(models.Model):
    reason = models.CharField(max_length=50, help_text='Motivo')
    funcionario = models.ForeignKey(Funcionario, on_delete=models.Prefetch)
    
    def __str__(self):
        return self.reason