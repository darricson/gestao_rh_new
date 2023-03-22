from django.db import models

# Create your models here.


class RegistroHoraExtra(models.Model):
    reason = models.CharField(max_length=50, help_text='Motivo')
    
    def __str__(self):
        return self.reason