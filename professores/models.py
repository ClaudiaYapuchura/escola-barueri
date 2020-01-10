from django.db import models
from ninjas.models import Ninja


# Create your models here.
class Professor(models.Model):
    nome = models.CharField(max_length=255)
    materia = models.CharField(max_length=255)
    idade = models.IntegerField()
    ninjas = models.ManyToManyField(Ninja)

    def __str__(self):
        return self.nome