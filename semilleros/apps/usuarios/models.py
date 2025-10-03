from django.contrib.auth.models import User
from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    numero_documento = models.CharField(max_length=100, unique=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
