from django.contrib import admin
from .models import Proveedor, FacturaCompra, DetalleFacturaCompra, Gasto

class DetalleFacturaCompraInline(admin.TabularInline):
    model = DetalleFacturaCompra
    extra = 1
    readonly_fields = ('subtotal',)
    fields = ('producto', 'cantidad', 'precio_unitario', 'precio_venta', 'subtotal')

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'contacto', 'telefono', 'email']

@admin.register(FacturaCompra)
class FacturaCompraAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'proveedor', 'fecha', 'total']
    list_filter = ('proveedor', 'fecha')
    search_fields = ('codigo', 'proveedor__nombre')
    inlines = [DetalleFacturaCompraInline]
    readonly_fields = ('total',)

@admin.register(Gasto)
class GastoAdmin(admin.ModelAdmin):
    list_display = ['descripcion', 'monto', 'fecha', 'tipo', 'factura']
    list_filter = ('tipo', 'fecha')
    search_fields = ('descripcion',)