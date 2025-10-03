from django.db import models
from apps.productos.models import Producto

class Seccion(models.Model):
    nombre = models.CharField(max_length=10, unique=True)  # A, B, C

    def __str__(self):
        return self.nombre

class Ubicacion(models.Model):
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE, related_name='ubicaciones')
    numero = models.IntegerField()  # 1, 2, 3
    codigo_completo = models.CharField(max_length=20, unique=True, editable=False)

    def save(self, *args, **kwargs):
        self.codigo_completo = f"{self.seccion.nombre}-{self.numero}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.codigo_completo

    class Meta:
        unique_together = ('seccion', 'numero')

class CategoriaInventario(models.Model):
    nombre = models.CharField(max_length=100, unique=True)  # tuercas, tornillos, herramientas

    def __str__(self):
        return self.nombre

class SubcategoriaInventario(models.Model):
    categoria = models.ForeignKey(CategoriaInventario, on_delete=models.CASCADE, related_name='subcategorias')
    nombre = models.CharField(max_length=100)  # tuerca alta, tuerca de seguridad

    def __str__(self):
        return f"{self.categoria.nombre} - {self.nombre}"

    class Meta:
        unique_together = ('categoria', 'nombre')

class InventarioItem(models.Model):
    subcategoria = models.ForeignKey(SubcategoriaInventario, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='inventario_items')
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE, related_name='items')
    stock_actual = models.IntegerField(default=0)
    stock_minimo = models.IntegerField(default=5)  # Para determinar amarillo

    def __str__(self):
        return f"{self.producto.nombre} en {self.ubicacion}"

    class Meta:
        unique_together = ('producto', 'ubicacion')  # Un producto por ubicación