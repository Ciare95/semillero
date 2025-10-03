from rest_framework import serializers
from .models import Seccion, Ubicacion, CategoriaInventario, SubcategoriaInventario, InventarioItem
from apps.productos.serializers import ProductoSerializer

class SeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seccion
        fields = ['id', 'nombre']

class UbicacionSerializer(serializers.ModelSerializer):
    seccion_detalle = SeccionSerializer(source='seccion', read_only=True)

    class Meta:
        model = Ubicacion
        fields = ['id', 'seccion', 'numero', 'codigo_completo', 'seccion_detalle']

class CategoriaInventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaInventario
        fields = ['id', 'nombre']

class SubcategoriaInventarioSerializer(serializers.ModelSerializer):
    categoria_detalle = CategoriaInventarioSerializer(source='categoria', read_only=True)

    class Meta:
        model = SubcategoriaInventario
        fields = ['id', 'categoria', 'nombre', 'categoria_detalle']

class InventarioItemSerializer(serializers.ModelSerializer):
    producto_detalle = ProductoSerializer(source='producto', read_only=True)
    ubicacion_detalle = UbicacionSerializer(source='ubicacion', read_only=True)
    subcategoria_detalle = SubcategoriaInventarioSerializer(source='subcategoria', read_only=True)

    class Meta:
        model = InventarioItem
        fields = [
            'id', 'subcategoria', 'producto', 'ubicacion', 'stock_actual', 'stock_minimo',
            'producto_detalle', 'ubicacion_detalle', 'subcategoria_detalle'
        ]