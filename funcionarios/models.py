from django.db import models

# Create your models here.


class Funcionario(models.Model):
    name = models.CharField(max_length=50, help_text='Nome do funcionario')
    
    def __str__(self):
        return self.name