# Generated by Django 4.1.7 on 2023-03-26 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos', '0002_departamento_empresas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='departamento',
            old_name='empresas',
            new_name='empresa',
        ),
    ]
