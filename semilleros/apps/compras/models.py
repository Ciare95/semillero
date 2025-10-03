from django.db import models
from apps.productos.models import Producto

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    contacto = models.CharField(max_length=100, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    direccion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class FacturaCompra(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='facturas')
    fecha = models.DateField()
    total = models.DecimalField(max_digits=14, decimal_places=2, default=0.00)
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"Factura {self.codigo} - {self.proveedor.nombre}"

class DetalleFacturaCompra(models.Model):
    factura = models.ForeignKey(FacturaCompra, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, help_text="Precio de venta (opcional)")
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.subtotal = self.precio_unitario * self.cantidad
        is_new = self.pk is None
        super().save(*args, **kwargs)
        if is_new:
            # Update product price and stock
            self.producto.precio_compra = self.precio_unitario
            if self.precio_venta is not None:
                self.producto.precio_venta = self.precio_venta
            self.producto.save()
            self.producto.add_stock(self.cantidad)
        # Update factura total
        self.factura.total = sum(d.subtotal for d in self.factura.detalles.all())
        self.factura.save(update_fields=['total'])

    def __str__(self):
        return f"{self.producto.nombre} x {self.cantidad}"

class Gasto(models.Model):
    descripcion = models.CharField(max_length=200)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()
    tipo = models.CharField(max_length=50, blank=True)  # transporte, etc.
    factura = models.ForeignKey(FacturaCompra, on_delete=models.SET_NULL, null=True, blank=True, related_name='gastos')

    def __str__(self):
        return f"{self.descripcion} - {self.monto}"