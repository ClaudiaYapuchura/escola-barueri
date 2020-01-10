from django.db import models

# Create your models here.
class Ninja(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.IntegerField()
    generos =(
        ('F', 'Feminino'),
        ('M', 'Masculimo'),
    )
    genero = models.CharField(max_length=2, choices=generos)
    email = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
