from django.contrib import admin
from decimal import Decimal
from django.core.exceptions import ValidationError
from .models import Venta, DetalleVenta, DetalleVentaEspecial, DetalleVentaServicio
from apps.productos.models import Producto, ProductoEspecial

class DetalleVentaInline(admin.TabularInline):
    model = DetalleVenta
    extra = 1
    readonly_fields = ('precio_unitario', 'iva_percent', 'subtotal', 'iva_valor', 'total_linea')

class DetalleVentaEspecialInline(admin.TabularInline):
    model = DetalleVentaEspecial
    extra = 1
    readonly_fields = ('precio_unitario', 'iva_percent', 'subtotal', 'iva_valor', 'total_linea')

class DetalleVentaServicioInline(admin.TabularInline):
    model = DetalleVentaServicio
    extra = 1
    readonly_fields = ('iva_percent', 'subtotal', 'iva_valor', 'total_linea')
    
@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha_hora', 'cliente', 'vendedor', 'total', 'estado', 'metodo_pago')
    list_filter = ('estado', 'metodo_pago', 'fecha_hora')
    readonly_fields = ('subtotal', 'iva_total', 'total')
    search_fields = ('cliente__nombre', 'vendedor__username')
    inlines = [DetalleVentaInline, DetalleVentaEspecialInline, DetalleVentaServicioInline]

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        venta = Venta.objects.get(pk=form.instance.pk)

        # Crear/actualizar detalles
        for det in instances:
            if isinstance(det, DetalleVenta):
                # Lógica para productos normales
                new_prod = det.producto
                new_qty = det.cantidad or 0

                # Si es edición, revertir stock previo del detalle
                if det.pk:
                    old = DetalleVenta.objects.get(pk=det.pk)
                    old_prod = old.producto
                    old_qty = old.cantidad

                    old_prod.restore_stock(old_qty)

                # Tomar valores del producto
                det.precio_unitario = new_prod.precio_venta
                det.iva_percent = new_prod.iva

                subtotal = det.precio_unitario * new_qty
                descuento_valor = subtotal * (det.descuento_percent / Decimal('100')) if det.descuento_percent else Decimal('0.00')
                base = subtotal - descuento_valor
                iva_valor = base * (det.iva_percent / Decimal('100'))
                total_linea = base + iva_valor

                det.subtotal = subtotal.quantize(Decimal('0.01'))
                det.iva_valor = iva_valor.quantize(Decimal('0.01'))
                det.total_linea = total_linea.quantize(Decimal('0.01'))

                # Aplicar nuevo stock
                try:
                    new_prod.deduct_stock(new_qty)
                except ValidationError as e:
                    raise ValidationError({'detalles': str(e)})

                det.save()
            elif isinstance(det, DetalleVentaEspecial):
                # Para productos especiales, solo guardar (cálculos en save del modelo)
                det.save()
            elif isinstance(det, DetalleVentaServicio):
                # Para productos de servicio, solo guardar (cálculos en save del modelo)
                det.save()

        # Manejar eliminaciones (devolver stock solo para productos normales)
        for obj in formset.deleted_objects:
            if isinstance(obj, DetalleVenta):
                prod = obj.producto
                prod.restore_stock(obj.cantidad)
            obj.delete()

        formset.save_m2m()

        # Recalcular totales de la venta (incluyendo detalles normales, especiales y servicios)
        subtotal_total = sum((d.subtotal for d in venta.detalles.all()), Decimal('0.00'))
        subtotal_total += sum((d.subtotal for d in venta.detalles_especiales.all()), Decimal('0.00'))
        subtotal_total += sum((d.subtotal for d in venta.detalles_servicio.all()), Decimal('0.00'))
        iva_total = sum((d.iva_valor for d in venta.detalles.all()), Decimal('0.00'))
        iva_total += sum((d.iva_valor for d in venta.detalles_especiales.all()), Decimal('0.00'))
        iva_total += sum((d.iva_valor for d in venta.detalles_servicio.all()), Decimal('0.00'))
        total_total = sum((d.total_linea for d in venta.detalles.all()), Decimal('0.00'))
        total_total += sum((d.total_linea for d in venta.detalles_especiales.all()), Decimal('0.00'))
        total_total += sum((d.total_linea for d in venta.detalles_servicio.all()), Decimal('0.00'))

        venta.subtotal = subtotal_total.quantize(Decimal('0.01'))
        venta.iva_total = iva_total.quantize(Decimal('0.01'))
        venta.total = total_total.quantize(Decimal('0.01'))
        venta.save()
