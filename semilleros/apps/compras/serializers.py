from decimal import Decimal
from django.db import transaction
from rest_framework import serializers
from .models import Proveedor, FacturaCompra, DetalleFacturaCompra, Gasto
from apps.productos.serializers import ProductoSerializer

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ['id', 'nombre', 'contacto', 'telefono', 'email', 'direccion']

class DetalleFacturaCompraCrearSerializer(serializers.Serializer):
    producto = serializers.IntegerField()
    cantidad = serializers.IntegerField(min_value=1)
    precio_unitario = serializers.DecimalField(max_digits=10, decimal_places=2)

class DetalleFacturaCompraDetalleSerializer(serializers.ModelSerializer):
    producto_detalle = ProductoSerializer(source='producto', read_only=True)

    class Meta:
        model = DetalleFacturaCompra
        fields = ['id', 'producto', 'producto_detalle', 'cantidad', 'precio_unitario', 'subtotal']

class FacturaCompraCrearSerializer(serializers.ModelSerializer):
    items = DetalleFacturaCompraCrearSerializer(many=True, write_only=True)

    class Meta:
        model = FacturaCompra
        fields = ['id', 'codigo', 'proveedor', 'fecha', 'observaciones', 'items']

    def validate(self, data):
        if not data.get('items'):
            raise serializers.ValidationError({'items': 'Debe enviar al menos un ítem'})
        return data

    @transaction.atomic
    def create(self, validated_data):
        items = validated_data.pop('items')
        factura = FacturaCompra.objects.create(**validated_data)

        total = Decimal('0.00')

        for item in items:
            producto_id = item['producto']
            cantidad = item['cantidad']
            precio_unitario = item['precio_unitario']

            try:
                from apps.productos.models import Producto
                producto = Producto.objects.get(id=producto_id)
            except Producto.DoesNotExist:
                raise serializers.ValidationError({'items': f'Producto {producto_id} no existe'})

            subtotal = precio_unitario * cantidad

            DetalleFacturaCompra.objects.create(
                factura=factura,
                producto=producto,
                cantidad=cantidad,
                precio_unitario=precio_unitario,
                subtotal=subtotal
            )

            # Actualizar precio de compra y stock
            producto.precio_compra = precio_unitario
            producto.save()
            producto.add_stock(cantidad)

            total += subtotal

        factura.total = total
        factura.save()

        return factura

class FacturaCompraDetalleSerializer(serializers.ModelSerializer):
    detalles = DetalleFacturaCompraDetalleSerializer(many=True, read_only=True)
    proveedor_detalle = ProveedorSerializer(source='proveedor', read_only=True)

    class Meta:
        model = FacturaCompra
        fields = ['id', 'codigo', 'proveedor', 'proveedor_detalle', 'fecha', 'total', 'observaciones', 'detalles']

class GastoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gasto
        fields = ['id', 'descripcion', 'monto', 'fecha', 'tipo', 'factura']