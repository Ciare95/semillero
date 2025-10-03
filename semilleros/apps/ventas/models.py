from decimal import Decimal
from django.db import models
from django.contrib.auth.models import User
from apps.usuarios.models import Cliente
from apps.productos.models import Producto, ProductoEspecial, ProductoServicio

class Venta(models.Model):
    class Estado(models.TextChoices):
        COMPLETADA = 'COMPLETADA', 'Completada'
        ANULADA = 'ANULADA', 'Anulada'
        
    class metodoPago(models.TextChoices):
        EFECTIVO = 'EFECTIVO', 'Efectivo'
        TARJETA = 'TARJETA', 'Tarjeta'
        TRANSFERENCIA = 'TRANSFERENCIA', 'Transferencia'
    
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, null=True, blank=True, related_name='ventas')
    vendedor = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True, related_name='ventas_realizadas')
    fecha_hora = models.DateTimeField(auto_now_add=True)
    
    subtotal = models.DecimalField(max_digits=14, decimal_places=2, default=Decimal('0.00'))
    iva_total = models.DecimalField(max_digits=14, decimal_places=2, default=Decimal('0.00'))
    total = models.DecimalField(max_digits=14, decimal_places=2, default=Decimal('0.00'))
    
    metodo_pago = models.CharField(max_length=20, choices=metodoPago.choices, default=metodoPago.EFECTIVO)
    estado = models.CharField(max_length=20, choices=Estado.choices, default=Estado.COMPLETADA)
    
    observaciones = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"Venta #{self.id} - {self.estado} - Total: {self.total}"


class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT, related_name='detalles_venta')
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=14, decimal_places=2)
    iva_percent = models.DecimalField(max_digits=5, decimal_places=2)
    descuento_percent = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    subtotal = models.DecimalField(max_digits=14, decimal_places=2, default=Decimal('0.00'))
    iva_valor = models.DecimalField(max_digits=14, decimal_places=2, default=Decimal('0.00'))
    total_linea = models.DecimalField(max_digits=14, decimal_places=2, default=Decimal('0.00'))
    
    def __str__(self):
        return f"{self.producto} x {self.cantidad}"


class DetalleVentaEspecial(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles_especiales')
    producto_especial = models.ForeignKey(ProductoEspecial, on_delete=models.PROTECT, related_name='detalles_venta_especial')
    ancho_corte = models.DecimalField(max_digits=10, decimal_places=2, help_text="Ancho del corte en cm")
    alto_corte = models.DecimalField(max_digits=10, decimal_places=2, help_text="Alto del corte en cm")
    precio_unitario = models.DecimalField(max_digits=14, decimal_places=2)  # precio por cm²
    iva_percent = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))  # assuming no IVA for special
    descuento_percent = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    subtotal = models.DecimalField(max_digits=14, decimal_places=2, default=Decimal('0.00'))
    iva_valor = models.DecimalField(max_digits=14, decimal_places=2, default=Decimal('0.00'))
    total_linea = models.DecimalField(max_digits=14, decimal_places=2, default=Decimal('0.00'))

    def save(self, *args, **kwargs):
        area = self.ancho_corte * self.alto_corte
        self.precio_unitario = self.producto_especial.precio_cm2
        subtotal = self.precio_unitario * area
        descuento_valor = subtotal * (self.descuento_percent / Decimal('100')) if self.descuento_percent else Decimal('0.00')
        base = subtotal - descuento_valor
        iva_valor = base * (self.iva_percent / Decimal('100'))
        self.subtotal = subtotal.quantize(Decimal('0.01'))
        self.iva_valor = iva_valor.quantize(Decimal('0.01'))
        self.total_linea = (base + iva_valor).quantize(Decimal('0.01'))
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.producto_especial} - {self.ancho_corte}cm x {self.alto_corte}cm"


class DetalleVentaServicio(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles_servicio')
    producto_servicio = models.ForeignKey(ProductoServicio, on_delete=models.PROTECT, related_name='detalles_venta_servicio')
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=14, decimal_places=2)
    iva_percent = models.DecimalField(max_digits=5, decimal_places=2)
    descuento_percent = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    subtotal = models.DecimalField(max_digits=14, decimal_places=2, default=Decimal('0.00'))
    iva_valor = models.DecimalField(max_digits=14, decimal_places=2, default=Decimal('0.00'))
    total_linea = models.DecimalField(max_digits=14, decimal_places=2, default=Decimal('0.00'))

    def save(self, *args, **kwargs):
        # precio_unitario is set by user, iva_percent = 0 for services
        self.iva_percent = Decimal('0.00')
        subtotal = self.precio_unitario * self.cantidad
        descuento_valor = subtotal * (self.descuento_percent / Decimal('100')) if self.descuento_percent else Decimal('0.00')
        base = subtotal - descuento_valor
        iva_valor = base * (self.iva_percent / Decimal('100'))
        self.subtotal = subtotal.quantize(Decimal('0.01'))
        self.iva_valor = iva_valor.quantize(Decimal('0.01'))
        self.total_linea = (base + iva_valor).quantize(Decimal('0.01'))
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.producto_servicio} x {self.cantidad}"
