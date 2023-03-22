from django.db import models

# Create your models here.


class Departamento(models.Model):
    name = models.CharField(max_length=70, help_text='Departamento')
    
    def __str__(self):
        return self.name