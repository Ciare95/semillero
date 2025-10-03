from django.db import models

class Reporte(models.Model):
    titulo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=50)  # e.g. 'ventas', 'productos', 'clientes'
    descripcion = models.TextField(null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    datos = models.JSONField(null=True, blank=True)  # Para almacenar datos del reporte si se guarda

    def __str__(self):
        return self.titulo