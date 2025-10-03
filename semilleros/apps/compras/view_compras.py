from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Proveedor, FacturaCompra, DetalleFacturaCompra, Gasto
from .serializers import ProveedorSerializer, FacturaCompraCrearSerializer, FacturaCompraDetalleSerializer, GastoSerializer

# Proveedores

@api_view(['GET'])
def obtenerProveedores(request):
    proveedores = Proveedor.objects.all()
    serializer = ProveedorSerializer(proveedores, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def crearProveedor(request):
    serializer = ProveedorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def actualizarProveedor(request, id):
    try:
        proveedor = Proveedor.objects.get(id=id)
    except Proveedor.DoesNotExist:
        return Response({'Error': 'Proveedor no encontrado'}, status=404)
    serializer = ProveedorSerializer(proveedor, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def eliminarProveedor(request, id):
    try:
        proveedor = Proveedor.objects.get(id=id)
    except Proveedor.DoesNotExist:
        return Response({'Error': 'Proveedor no encontrado'}, status=404)
    serializer = ProveedorSerializer(proveedor)
    proveedor.delete()
    return Response({'Mensaje': 'Proveedor eliminado', 'proveedor': serializer.data}, status=200)

# Facturas Compra

@api_view(['GET'])
def obtenerFacturasCompra(request):
    facturas = FacturaCompra.objects.all().order_by('-id')
    serializer = FacturaCompraDetalleSerializer(facturas, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def obtenerFacturaCompra(request, id):
    try:
        factura = FacturaCompra.objects.get(id=id)
    except FacturaCompra.DoesNotExist:
        return Response({'error': 'Factura no encontrada'}, status=404)
    return Response(FacturaCompraDetalleSerializer(factura).data)

@api_view(['POST'])
def crearFacturaCompra(request):
    serializer = FacturaCompraCrearSerializer(data=request.data)
    if serializer.is_valid():
        factura = serializer.save()
        return Response(FacturaCompraDetalleSerializer(factura).data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def actualizarFacturaCompra(request, id):
    # Para simplicidad, no implementar actualización completa, solo campos básicos
    try:
        factura = FacturaCompra.objects.get(id=id)
    except FacturaCompra.DoesNotExist:
        return Response({'Error': 'Factura no encontrada'}, status=404)
    serializer = FacturaCompraCrearSerializer(factura, data=request.data)
    if serializer.is_valid():
        factura = serializer.save()
        return Response(FacturaCompraDetalleSerializer(factura).data)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def eliminarFacturaCompra(request, id):
    try:
        factura = FacturaCompra.objects.get(id=id)
    except FacturaCompra.DoesNotExist:
        return Response({'Error': 'Factura no encontrada'}, status=404)
    serializer = FacturaCompraDetalleSerializer(factura)
    # Revertir stock y precios? Para simplicidad, no
    factura.delete()
    return Response({'Mensaje': 'Factura eliminada', 'factura': serializer.data}, status=200)

# Gastos

@api_view(['GET'])
def obtenerGastos(request):
    gastos = Gasto.objects.all().order_by('-fecha')
    serializer = GastoSerializer(gastos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def crearGasto(request):
    serializer = GastoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def actualizarGasto(request, id):
    try:
        gasto = Gasto.objects.get(id=id)
    except Gasto.DoesNotExist:
        return Response({'Error': 'Gasto no encontrado'}, status=404)
    serializer = GastoSerializer(gasto, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def eliminarGasto(request, id):
    try:
        gasto = Gasto.objects.get(id=id)
    except Gasto.DoesNotExist:
        return Response({'Error': 'Gasto no encontrado'}, status=404)
    serializer = GastoSerializer(gasto)
    gasto.delete()
    return Response({'Mensaje': 'Gasto eliminado', 'gasto': serializer.data}, status=200)