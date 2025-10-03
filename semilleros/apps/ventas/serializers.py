from decimal import Decimal
from django.db import transaction
from rest_framework import serializers
from django.core.exceptions import ValidationError
from apps.productos.models import Producto, ProductoEspecial, ProductoServicio
from .models import Venta, DetalleVenta, DetalleVentaEspecial, DetalleVentaServicio
from apps.productos.serializers import ProductoSerializer, ProductoEspecialSerializer, ProductoServicioSerializer

class DetalleVentaCrearSerializer(serializers.Serializer):
    producto = serializers.IntegerField()
    cantidad = serializers.IntegerField(min_value=1)
    descuento_percent = serializers.DecimalField(max_digits=5, decimal_places=2, required=False, default=Decimal('0.00'))
    
class DetalleVentaDetalleSerializer(serializers.ModelSerializer):
    producto_detalle = ProductoSerializer(source='producto', read_only=True)

    class Meta:
        model = DetalleVenta
        fields = [
            'id', 'producto', 'producto_detalle', 'cantidad',
            'precio_unitario', 'iva_percent', 'descuento_percent',
            'subtotal', 'iva_valor', 'total_linea'
        ]


class DetalleVentaEspecialCrearSerializer(serializers.Serializer):
    producto_especial = serializers.IntegerField()
    ancho_corte = serializers.DecimalField(max_digits=10, decimal_places=2)
    alto_corte = serializers.DecimalField(max_digits=10, decimal_places=2)
    descuento_percent = serializers.DecimalField(max_digits=5, decimal_places=2, required=False, default=Decimal('0.00'))


class DetalleVentaEspecialDetalleSerializer(serializers.ModelSerializer):
    producto_especial_detalle = ProductoEspecialSerializer(source='producto_especial', read_only=True)

    class Meta:
        model = DetalleVentaEspecial
        fields = [
            'id', 'producto_especial', 'producto_especial_detalle', 'ancho_corte', 'alto_corte',
            'precio_unitario', 'iva_percent', 'descuento_percent',
            'subtotal', 'iva_valor', 'total_linea'
        ]


class DetalleVentaServicioCrearSerializer(serializers.Serializer):
    producto_servicio = serializers.IntegerField()
    cantidad = serializers.IntegerField(min_value=1)
    precio_unitario = serializers.DecimalField(max_digits=14, decimal_places=2)
    descuento_percent = serializers.DecimalField(max_digits=5, decimal_places=2, required=False, default=Decimal('0.00'))


class DetalleVentaServicioDetalleSerializer(serializers.ModelSerializer):
    producto_servicio_detalle = ProductoServicioSerializer(source='producto_servicio', read_only=True)

    class Meta:
        model = DetalleVentaServicio
        fields = [
            'id', 'producto_servicio', 'producto_servicio_detalle', 'cantidad',
            'precio_unitario', 'iva_percent', 'descuento_percent',
            'subtotal', 'iva_valor', 'total_linea'
        ]

class VentaCrearSerializer(serializers.ModelSerializer):
    items = DetalleVentaCrearSerializer(many=True, write_only=True, required=False)
    items_especiales = DetalleVentaEspecialCrearSerializer(many=True, write_only=True, required=False)
    items_servicio = DetalleVentaServicioCrearSerializer(many=True, write_only=True, required=False)

    class Meta:
        model = Venta
        fields = ['id', 'cliente', 'metodo_pago', 'observaciones', 'items', 'items_especiales', 'items_servicio']
        
    def validate(self, data):
        items = data.get('items', [])
        items_especiales = data.get('items_especiales', [])
        items_servicio = data.get('items_servicio', [])
        if not items and not items_especiales and not items_servicio:
            raise serializers.ValidationError({'items': 'Debe enviar al menos un ítem'})
        return data
    
    @transaction.atomic
    def create(self, validate_data):
        request = self.context.get('request')
        items = validate_data.pop('items', [])
        items_especiales = validate_data.pop('items_especiales', [])
        items_servicio = validate_data.pop('items_servicio', [])
        venta = Venta.objects.create(
            cliente = validate_data.get('cliente'),
            vendedor = getattr(request, 'user', None) if request and request.user and request.user.is_authenticated else None,
            metodo_pago = validate_data.get('metodo_pago', Venta.metodoPago.EFECTIVO),
            observaciones = validate_data.get('observaciones', '')
        )

        subtotal_total = Decimal('0.00')
        iva_total = Decimal('0.00')
        total_total = Decimal('0.00')

        # Procesar items normales
        for item in items:
            producto_id = item['producto']
            cantidad = item['cantidad']
            descuento_percent = item.get('descuento_percent', Decimal('0.00'))

            try:
                producto = Producto.objects.select_for_update().get(id=producto_id)
            except Producto.DoesNotExist:
                raise serializers.ValidationError({'Items': f'Producto {producto_id} no existe'})

            if producto.stock < cantidad:
                raise serializers.ValidationError({'items': f'Sin stock suficiente para {producto.nombre}. Stock: {producto.stock}'})

            precio_unitario = producto.precio_venta
            iva_percent = producto.iva
            subtotal = (precio_unitario * cantidad)
            descuento_valor = (subtotal * (descuento_percent / Decimal('100'))) if descuento_percent else Decimal('0.00')
            base_gravable = subtotal - descuento_valor
            iva_valor = base_gravable * (iva_percent / Decimal('100'))
            total_linea = base_gravable + iva_valor

            DetalleVenta.objects.create(
                venta = venta,
                producto = producto,
                cantidad = cantidad,
                precio_unitario = precio_unitario,
                iva_percent = iva_percent,
                descuento_percent = descuento_percent,
                subtotal = subtotal.quantize(Decimal('0.01')),
                iva_valor = iva_valor.quantize(Decimal('0.01')),
                total_linea = total_linea.quantize(Decimal('0.01'))
            )

            producto.deduct_stock(cantidad)

            subtotal_total += subtotal
            iva_total += iva_valor
            total_total += total_linea

        # Procesar items especiales
        for item in items_especiales:
            producto_especial_id = item['producto_especial']
            ancho_corte = item['ancho_corte']
            alto_corte = item['alto_corte']
            descuento_percent = item.get('descuento_percent', Decimal('0.00'))

            try:
                producto_especial = ProductoEspecial.objects.get(id=producto_especial_id)
            except ProductoEspecial.DoesNotExist:
                raise serializers.ValidationError({'items_especiales': f'Producto especial {producto_especial_id} no existe'})

            # Crear detalle especial (cálculos en save)
            detalle_especial = DetalleVentaEspecial(
                venta=venta,
                producto_especial=producto_especial,
                ancho_corte=ancho_corte,
                alto_corte=alto_corte,
                descuento_percent=descuento_percent
            )
            detalle_especial.save()

            subtotal_total += detalle_especial.subtotal
            iva_total += detalle_especial.iva_valor
            total_total += detalle_especial.total_linea

        # Procesar items de servicio
        for item in items_servicio:
            producto_servicio_id = item['producto_servicio']
            cantidad = item['cantidad']
            precio_unitario = item['precio_unitario']
            descuento_percent = item.get('descuento_percent', Decimal('0.00'))

            try:
                producto_servicio = ProductoServicio.objects.get(id=producto_servicio_id)
            except ProductoServicio.DoesNotExist:
                raise serializers.ValidationError({'items_servicio': f'Producto servicio {producto_servicio_id} no existe'})

            # Crear detalle servicio (cálculos en save)
            detalle_servicio = DetalleVentaServicio(
                venta=venta,
                producto_servicio=producto_servicio,
                cantidad=cantidad,
                precio_unitario=precio_unitario,
                descuento_percent=descuento_percent
            )
            detalle_servicio.save()

            subtotal_total += detalle_servicio.subtotal
            iva_total += detalle_servicio.iva_valor
            total_total += detalle_servicio.total_linea

        venta.subtotal = subtotal_total.quantize(Decimal('0.01'))
        venta.iva_total = iva_total.quantize(Decimal('0.01'))
        venta.total = total_total.quantize(Decimal('0.01'))
        venta.full_clean()
        venta.save()

        return venta
    
class VentaDetalleSerializer(serializers.ModelSerializer):
    detalles = DetalleVentaDetalleSerializer(many=True, read_only=True)
    detalles_especiales = DetalleVentaEspecialDetalleSerializer(many=True, read_only=True)
    detalles_servicio = DetalleVentaServicioDetalleSerializer(many=True, read_only=True)

    class Meta:
        model = Venta
        fields = [
        'id', 'cliente', 'vendedor', 'fecha_hora',
        'subtotal', 'iva_total', 'total',
        'metodo_pago', 'estado', 'observaciones',
        'detalles', 'detalles_especiales', 'detalles_servicio'
        ]
