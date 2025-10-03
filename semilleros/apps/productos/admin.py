from django.contrib import admin
from .models import Producto, Categoria, Marca, ProductoEspecial, ProductoServicio

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'stock', 'marca', 'precio_compra', 'precio_venta', 'iva', 'fecha_ingreso', 'categoria']
    
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion']
    
@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion']

@admin.register(ProductoEspecial)
class ProductoEspecialAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'ancho_material', 'alto_material', 'precio_total', 'porcentaje', 'costo_cm2', 'precio_cm2', 'categoria', 'marca']

@admin.register(ProductoServicio)
class ProductoServicioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'categoria', 'marca']