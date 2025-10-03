from django.db import transaction
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from .models import Venta
from .serializers import VentaCrearSerializer, VentaDetalleSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def listarVentas(request):
    """
    Lista todas las ventas con filtros opcionales.
    
    Parámetros de consulta (query parameters):
    - cliente_id: Filtrar por ID de cliente
    - estado: Filtrar por estado de venta (ej: COMPLETADA, PENDIENTE, ANULADA)
    - fecha_desde: Filtrar desde esta fecha (YYYY-MM-DD)
    - fecha_hasta: Filtrar hasta esta fecha (YYYY-MM-DD)
    
    La respuesta incluye los detalles de cada venta (productos vendidos).
    
    Ejemplo: /ventas/?cliente_id=1&estado=COMPLETADA&fecha_desde=2024-01-01&fecha_hasta=2024-12-31
    """
    
    # Obtener todas las ventas ordenadas por ID descendente (más recientes primero)
    consulta_ventas = Venta.objects.all().order_by('-id')
    
    # Filtrar por cliente si se proporciona el parámetro
    cliente_id = request.query_params.get('cliente_id')
    if cliente_id:
        consulta_ventas = consulta_ventas.filter(cliente_id=cliente_id)
    
    # Filtrar por estado si se proporciona el parámetro
    estado_venta = request.query_params.get('estado')
    if estado_venta:
        consulta_ventas = consulta_ventas.filter(estado=estado_venta)
    
    # Filtrar por rango de fechas si se proporcionan los parámetros
    fecha_desde = request.query_params.get('fecha_desde')
    fecha_hasta = request.query_params.get('fecha_hasta')
    
    if fecha_desde:
        consulta_ventas = consulta_ventas.filter(fecha_hora__date__gte=fecha_desde)
    if fecha_hasta:
        consulta_ventas = consulta_ventas.filter(fecha_hora__date__lte=fecha_hasta)
    
    # Serializar los datos y retornar la respuesta
    datos_serializados = VentaDetalleSerializer(consulta_ventas, many=True).data
    return Response(datos_serializados)

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def obtener_venta(request, id):
    try:
        venta = Venta.objects.get(id=id)
    except Venta.DoesNotExist:
        return Response({'error': 'Venta no encontrada'}, status=404)
    return Response(VentaDetalleSerializer(venta).data)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def crearVenta(request):
    
    serializer = VentaCrearSerializer(data=request.data, context={'request':request})
    if serializer.is_valid():
        venta = serializer.save()
        return Response(VentaDetalleSerializer(venta).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
@transaction.atomic
def anularVenta(request, id):
    try:
        venta = Venta.objects.select_for_update().get(id=id)
    except Venta.DoesNotExist:
        return Response({'error': 'Venta no encontrada'}, status=404)
    
    if venta.estado == Venta.Estado.ANULADA:
        return Response({'error': 'La venta ya está anulada'}, status=400)
    
    # Revertir stock de cada detalle
    for det in venta.detalles.select_related('producto').all():
        prod = det.producto
        prod.restore_stock(det.cantidad)
        
    venta.estado = Venta.Estado.ANULADA
    venta.save()
    return Response({'mensaje': 'Venta anulada correctamente'})
