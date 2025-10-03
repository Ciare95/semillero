from django.db import models
from django.core.exceptions import ValidationError

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.nombre
    
class Marca(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(null=True, blank=True)
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=20, decimal_places=2)
    iva = models.DecimalField(max_digits=5, decimal_places=2, help_text="Porcentaje de IVA ej: 19.00")
    fecha_ingreso = models.DateField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, related_name="productos")
    marca = models.ForeignKey(Marca, on_delete=models.SET_NULL, null=True, blank=True, related_name="productos")

    @property
    def stock(self):
        return sum(self.inventario_items.values_list('stock_actual', flat=True)) or 0

    def deduct_stock(self, cantidad):
        # Asegura que exista un InventarioItem; valida stock suficiente
        from apps.inventario.models import InventarioItem  # import local para evitar ciclos
        item = self.inventario_items.first()
        if not item:
            # No creamos ítem automáticamente aquí para evitar descontar desde 0 sin control
            raise ValidationError(f"Producto sin ítem de inventario configurado para {self.nombre}")
        if item.stock_actual < cantidad:
            raise ValidationError(f"Stock insuficiente en bodega para {self.nombre}")
        item.stock_actual -= cantidad
        item.save()

    def restore_stock(self, cantidad):
        # Aumenta stock; si no existe InventarioItem se crea con defaults
        from apps.inventario.models import InventarioItem, Ubicacion, SubcategoriaInventario  # import local para evitar ciclos
        item = self.inventario_items.first()
        if not item:
            ubicacion = Ubicacion.objects.first()
            subcategoria = SubcategoriaInventario.objects.first()
            if not ubicacion or not subcategoria:
                raise ValidationError('Debe crear al menos una Ubicación y una Subcategoría de inventario para registrar stock.')
            item = InventarioItem.objects.create(
                producto=self,
                ubicacion=ubicacion,
                subcategoria=subcategoria,
                stock_actual=0
            )
        item.stock_actual += cantidad
        item.save()

    def add_stock(self, cantidad):
        # Aumenta stock; si no existe InventarioItem se crea con defaults
        from apps.inventario.models import InventarioItem, Ubicacion, SubcategoriaInventario  # import local para evitar ciclos
        item = self.inventario_items.first()
        if not item:
            ubicacion = Ubicacion.objects.first()
            subcategoria = SubcategoriaInventario.objects.first()
            if not ubicacion or not subcategoria:
                raise ValidationError('Debe crear al menos una Ubicación y una Subcategoría de inventario para registrar stock.')
            item = InventarioItem.objects.create(
                producto=self,
                ubicacion=ubicacion,
                subcategoria=subcategoria,
                stock_actual=0
            )
        item.stock_actual += cantidad
        item.save()

    def clean(self):
        if self.precio_venta < self.precio_compra:
            raise ValidationError('El precio de venta debe ser mayor al precio de compra')

    def __str__(self):
        return f"{self.nombre} ({self.marca})"


class ProductoEspecial(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(null=True, blank=True)
    ancho_material = models.DecimalField(max_digits=10, decimal_places=2, help_text="Ancho en cm")
    alto_material = models.DecimalField(max_digits=10, decimal_places=2, help_text="Alto en cm")
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, help_text="Costo total de la lámina o rollo")
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2, help_text="Porcentaje de ganancia")
    costo_cm2 = models.DecimalField(max_digits=10, decimal_places=4, editable=False)
    precio_cm2 = models.DecimalField(max_digits=10, decimal_places=4, editable=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, related_name="productos_especiales")
    marca = models.ForeignKey(Marca, on_delete=models.SET_NULL, null=True, blank=True, related_name="productos_especiales")

    def save(self, *args, **kwargs):
        area = self.ancho_material * self.alto_material
        if area == 0:
            raise ValidationError("El área del material no puede ser cero.")
        self.costo_cm2 = self.precio_total / area
        self.precio_cm2 = self.costo_cm2 * (1 + self.porcentaje / 100)
        super().save(*args, **kwargs)

    def calcular_precio_corte(self, ancho_corte, alto_corte):
        area_corte = ancho_corte * alto_corte
        return self.precio_cm2 * area_corte

    def __str__(self):
        return f"{self.nombre} (Especial)"


class ProductoServicio(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, related_name="productos_servicio")
    marca = models.ForeignKey(Marca, on_delete=models.SET_NULL, null=True, blank=True, related_name="productos_servicio")

    def __str__(self):
        return f"{self.nombre} (Servicio)"
