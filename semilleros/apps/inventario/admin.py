from django.contrib import admin
from .models import Seccion, Ubicacion, CategoriaInventario, SubcategoriaInventario, InventarioItem

@admin.register(Seccion)
class SeccionAdmin(admin.ModelAdmin):
    list_display = ['nombre']

@admin.register(Ubicacion)
class UbicacionAdmin(admin.ModelAdmin):
    list_display = ['codigo_completo', 'seccion', 'numero']

@admin.register(CategoriaInventario)
class CategoriaInventarioAdmin(admin.ModelAdmin):
    list_display = ['nombre']

@admin.register(SubcategoriaInventario)
class SubcategoriaInventarioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'categoria']

@admin.register(InventarioItem)
class InventarioItemAdmin(admin.ModelAdmin):
    list_display = ['producto', 'ubicacion', 'stock_actual', 'stock_minimo']