from rest_framework import serializers
from django.core.exceptions import ValidationError
from .models import Categoria, Marca, Producto, ProductoEspecial, ProductoServicio

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'descripcion']
        
class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ['id', 'nombre', 'descripcion']
        
class ProductoSerializer(serializers.ModelSerializer):
    categoria_detalle = CategoriaSerializer(source='categoria', read_only=True)
    marca_detalle = MarcaSerializer(source='marca', read_only=True)
    stock = serializers.ReadOnlyField()

    class Meta:
        model = Producto
        fields = [
            'id',
            'nombre',
            'descripcion',
            'stock',
            'precio_compra',
            'precio_venta',
            'iva',
            'fecha_ingreso',
            'categoria',
            'marca',
            'categoria_detalle',
            'marca_detalle'
        ]

    def validate(self, data):
        # Ejecutar la validación del modelo
        producto = Producto(**data)
        try:
            producto.full_clean()
        except ValidationError as e:
            raise serializers.ValidationError(e.message_dict)

        return data


class ProductoServicioSerializer(serializers.ModelSerializer):
    categoria_detalle = CategoriaSerializer(source='categoria', read_only=True)
    marca_detalle = MarcaSerializer(source='marca', read_only=True)

    class Meta:
        model = ProductoServicio
        fields = [
            'id',
            'nombre',
            'descripcion',
            'categoria',
            'marca',
            'categoria_detalle',
            'marca_detalle'
        ]

    def validate(self, data):
        # Ejecutar la validación del modelo
        producto_servicio = ProductoServicio(**data)
        try:
            producto_servicio.full_clean()
        except ValidationError as e:
            raise serializers.ValidationError(e.message_dict)

        return data


class ProductoEspecialSerializer(serializers.ModelSerializer):
    categoria_detalle = CategoriaSerializer(source='categoria', read_only=True)
    marca_detalle = MarcaSerializer(source='marca', read_only=True)

    class Meta:
        model = ProductoEspecial
        fields = [
            'id',
            'nombre',
            'descripcion',
            'ancho_material',
            'alto_material',
            'precio_total',
            'porcentaje',
            'costo_cm2',
            'precio_cm2',
            'categoria',
            'marca',
            'categoria_detalle',
            'marca_detalle'
        ]
        read_only_fields = ['costo_cm2', 'precio_cm2']

    def validate(self, data):
        # Ejecutar la validación del modelo
        producto_especial = ProductoEspecial(**data)
        try:
            producto_especial.full_clean()
        except ValidationError as e:
            raise serializers.ValidationError(e.message_dict)

        return data
