from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Reporte
from .serializers import ReporteSerializer
from django.db.models import Sum, Count
from apps.ventas.models import Venta
from apps.productos.models import Producto
from apps.usuarios.models import Cliente
from apps.compras.models import FacturaCompra, Gasto
from decimal import Decimal


# Obtener o leer todo lo relacionado a reportes

@api_view(['GET'])
def obtenerReportes(request):
    reportes = Reporte.objects.all()
    serializer = ReporteSerializer(reportes, many=True)
    return Response(serializer.data)


# Crear todo lo relacionado a reportes

@api_view(['POST'])
def crearReporte(request):
    serializer = ReporteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=400)


# Reportes específicos

@api_view(['GET'])
def reporteVentas(request):
    # Total de ventas completadas
    total_ventas = Venta.objects.filter(estado='COMPLETADA').aggregate(total=Sum('total'))['total'] or 0
    return Response({'total_ventas': total_ventas})

@api_view(['GET'])
def reporteProductos(request):
    # Productos con stock bajo (menos de 10)
    productos_bajo_stock = Producto.objects.filter(stock__lt=10).values('nombre', 'stock')
    return Response(list(productos_bajo_stock))

@api_view(['GET'])
def reporteClientes(request):
    # Top clientes por total de ventas
    top_clientes = Cliente.objects.annotate(total_ventas=Sum('ventas__total')).filter(total_ventas__isnull=False).order_by('-total_ventas')[:5]
    data = [{'cliente': c.nombre, 'total': c.total_ventas} for c in top_clientes]
    return Response(data)

@api_view(['GET'])
def ingresosGastos(request):
    """
    Endpoint de finanzas: ingresos y gastos.
    - Ingresos: sumatoria de ventas COMPLETADAS (Venta.total).
    - Gastos: sumatoria de FacturaCompra.total + Gasto.monto.
    Filtros opcionales por rango de fechas:
      - fecha_desde (YYYY-MM-DD)
      - fecha_hasta (YYYY-MM-DD)
    Para ventas se filtra por venta.fecha_hora__date.
    Para compras/gastos se filtra por su campo fecha.
    """
    fecha_desde = request.query_params.get('fecha_desde')
    fecha_hasta = request.query_params.get('fecha_hasta')

    # Ingresos por ventas completadas
    ventas_qs = Venta.objects.filter(estado=Venta.Estado.COMPLETADA)
    if fecha_desde:
        ventas_qs = ventas_qs.filter(fecha_hora__date__gte=fecha_desde)
    if fecha_hasta:
        ventas_qs = ventas_qs.filter(fecha_hora__date__lte=fecha_hasta)
    ingresos_ventas = ventas_qs.aggregate(total=Sum('total'))['total'] or Decimal('0.00')

    # Gastos: compras (facturas) + otros gastos
    compras_qs = FacturaCompra.objects.all()
    if fecha_desde:
        compras_qs = compras_qs.filter(fecha__gte=fecha_desde)
    if fecha_hasta:
        compras_qs = compras_qs.filter(fecha__lte=fecha_hasta)
    gastos_compras = compras_qs.aggregate(total=Sum('total'))['total'] or Decimal('0.00')

    gastos_qs = Gasto.objects.all()
    if fecha_desde:
        gastos_qs = gastos_qs.filter(fecha__gte=fecha_desde)
    if fecha_hasta:
        gastos_qs = gastos_qs.filter(fecha__lte=fecha_hasta)
    gastos_varios = gastos_qs.aggregate(total=Sum('monto'))['total'] or Decimal('0.00')

    gastos_total = gastos_compras + gastos_varios
    balance = ingresos_ventas - gastos_total

    data = {
        'fecha_desde': fecha_desde,
        'fecha_hasta': fecha_hasta,
        'ingresos': {
            'ventas_total': ingresos_ventas,
        },
        'gastos': {
            'compras_total': gastos_compras,
            'gastos_total': gastos_varios,
        },
        'totales': {
            'ingresos': ingresos_ventas,
            'gastos': gastos_total,
            'balance': balance,
        }
    }
    return Response(data)
