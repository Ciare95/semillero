from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Seccion, Ubicacion, CategoriaInventario, SubcategoriaInventario, InventarioItem
from .serializers import SeccionSerializer, UbicacionSerializer, CategoriaInventarioSerializer, SubcategoriaInventarioSerializer, InventarioItemSerializer

# Secciones

@api_view(['GET'])
def obtenerSecciones(request):
    secciones = Seccion.objects.all()
    serializer = SeccionSerializer(secciones, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def crearSeccion(request):
    serializer = SeccionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def actualizarSeccion(request, id):
    try:
        seccion = Seccion.objects.get(id=id)
    except Seccion.DoesNotExist:
        return Response({'Error': 'Sección no encontrada'}, status=404)
    serializer = SeccionSerializer(seccion, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def eliminarSeccion(request, id):
    try:
        seccion = Seccion.objects.get(id=id)
    except Seccion.DoesNotExist:
        return Response({'Error': 'Sección no encontrada'}, status=404)
    serializer = SeccionSerializer(seccion)
    seccion.delete()
    return Response({'Mensaje': 'Sección eliminada', 'seccion': serializer.data}, status=200)

# Ubicaciones

@api_view(['GET'])
def obtenerUbicaciones(request):
    ubicaciones = Ubicacion.objects.all()
    serializer = UbicacionSerializer(ubicaciones, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def crearUbicacion(request):
    serializer = UbicacionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def actualizarUbicacion(request, id):
    try:
        ubicacion = Ubicacion.objects.get(id=id)
    except Ubicacion.DoesNotExist:
        return Response({'Error': 'Ubicación no encontrada'}, status=404)
    serializer = UbicacionSerializer(ubicacion, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def eliminarUbicacion(request, id):
    try:
        ubicacion = Ubicacion.objects.get(id=id)
    except Ubicacion.DoesNotExist:
        return Response({'Error': 'Ubicación no encontrada'}, status=404)
    serializer = UbicacionSerializer(ubicacion)
    ubicacion.delete()
    return Response({'Mensaje': 'Ubicación eliminada', 'ubicacion': serializer.data}, status=200)

# Categorias Inventario

@api_view(['GET'])
def obtenerCategoriasInventario(request):
    categorias = CategoriaInventario.objects.all()
    serializer = CategoriaInventarioSerializer(categorias, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def crearCategoriaInventario(request):
    serializer = CategoriaInventarioSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def actualizarCategoriaInventario(request, id):
    try:
        categoria = CategoriaInventario.objects.get(id=id)
    except CategoriaInventario.DoesNotExist:
        return Response({'Error': 'Categoría no encontrada'}, status=404)
    serializer = CategoriaInventarioSerializer(categoria, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def eliminarCategoriaInventario(request, id):
    try:
        categoria = CategoriaInventario.objects.get(id=id)
    except CategoriaInventario.DoesNotExist:
        return Response({'Error': 'Categoría no encontrada'}, status=404)
    serializer = CategoriaInventarioSerializer(categoria)
    categoria.delete()
    return Response({'Mensaje': 'Categoría eliminada', 'categoria': serializer.data}, status=200)

# Subcategorias Inventario

@api_view(['GET'])
def obtenerSubcategoriasInventario(request):
    subcategorias = SubcategoriaInventario.objects.all()
    serializer = SubcategoriaInventarioSerializer(subcategorias, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def crearSubcategoriaInventario(request):
    serializer = SubcategoriaInventarioSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def actualizarSubcategoriaInventario(request, id):
    try:
        subcategoria = SubcategoriaInventario.objects.get(id=id)
    except SubcategoriaInventario.DoesNotExist:
        return Response({'Error': 'Subcategoría no encontrada'}, status=404)
    serializer = SubcategoriaInventarioSerializer(subcategoria, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def eliminarSubcategoriaInventario(request, id):
    try:
        subcategoria = SubcategoriaInventario.objects.get(id=id)
    except SubcategoriaInventario.DoesNotExist:
        return Response({'Error': 'Subcategoría no encontrada'}, status=404)
    serializer = SubcategoriaInventarioSerializer(subcategoria)
    subcategoria.delete()
    return Response({'Mensaje': 'Subcategoría eliminada', 'subcategoria': serializer.data}, status=200)

# Inventario Items

@api_view(['GET'])
def obtenerInventarioItems(request):
    items = InventarioItem.objects.all()
    serializer = InventarioItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def crearInventarioItem(request):
    serializer = InventarioItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def actualizarInventarioItem(request, id):
    try:
        item = InventarioItem.objects.get(id=id)
    except InventarioItem.DoesNotExist:
        return Response({'Error': 'Ítem no encontrado'}, status=404)
    serializer = InventarioItemSerializer(item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def eliminarInventarioItem(request, id):
    try:
        item = InventarioItem.objects.get(id=id)
    except InventarioItem.DoesNotExist:
        return Response({'Error': 'Ítem no encontrado'}, status=404)
    serializer = InventarioItemSerializer(item)
    item.delete()
    return Response({'Mensaje': 'Ítem eliminado', 'item': serializer.data}, status=200)

# Vista especial para obtener inventario por categorías (como hojas de Excel)

@api_view(['GET'])
def obtenerInventarioPorCategoria(request):
    categorias = CategoriaInventario.objects.prefetch_related('subcategorias__items__producto', 'subcategorias__items__ubicacion').all()
    data = []
    for categoria in categorias:
        cat_data = {
            'categoria': categoria.nombre,
            'subcategorias': []
        }
        for subcategoria in categoria.subcategorias.all():
            sub_data = {
                'subcategoria': subcategoria.nombre,
                'items': []
            }
            for item in subcategoria.items.all():
                item_data = {
                    'producto': item.producto.nombre,
                    'codigo': item.producto.nombre,  # Asumiendo que el código es el nombre, o agregar campo
                    'ubicacion': item.ubicacion.codigo_completo,
                    'stock_actual': item.stock_actual,
                    'stock_minimo': item.stock_minimo,
                    'estado': 'verde' if item.stock_actual > item.stock_minimo else 'amarillo' if item.stock_actual > 0 else 'rojo'
                }
                sub_data['items'].append(item_data)
            cat_data['subcategorias'].append(sub_data)
        data.append(cat_data)
    return Response(data)