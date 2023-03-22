from django.db import models

# Create your models here.


class Documento(models.Model):
    description = models.CharField(max_length=100, help_text='Descrição')
    
    def __str__(self):
        return self.description