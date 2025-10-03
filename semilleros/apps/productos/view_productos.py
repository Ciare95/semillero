from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Categoria, Marca, Producto, ProductoEspecial, ProductoServicio
from .serializers import CategoriaSerializer, MarcaSerializer, ProductoSerializer, ProductoEspecialSerializer, ProductoServicioSerializer


# Obtener o leer todo lo relacionado a productos

@api_view(['GET'])
def obtenerProductos(request):
    # Buscar en la base de datos
    productos = Producto.objects.all()
    
    # Pasarlo a JSON
    serializer = ProductoSerializer(productos, many=True)
    
    # Retornar respuesta
    return Response(serializer.data)

@api_view(['GET'])
def obtenerProducto(request, id):
    try:
        producto = Producto.objects.get(id=id)
    except Producto.DoesNotExist:
        return Response({'Error': 'Producto no encontrado'}, status=404)
    serializer = ProductoSerializer(producto)
    return Response(serializer.data)

@api_view(['GET'])
def obtenerMarcas(request):
    marca = Marca.objects.all()    
    serializer = MarcaSerializer(marca, many=True)    
    return Response(serializer.data)

@api_view(['GET'])
def obtenerCategorias(request):
    categoria = Categoria.objects.all()    
    serializer = CategoriaSerializer(categoria, many=True)    
    return Response(serializer.data)


# Crear todo lo relacionado a productos

@api_view(['POST'])
def crearProducto(request):    
    serializer = ProductoSerializer(data=request.data)    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=400)
    
@api_view(['POST'])
def crearCategoria(request):    
    serializer = CategoriaSerializer(data=request.data)    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=400)
    
@api_view(['POST'])
def crearMarca(request):
    serializer = MarcaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=400)
    

# Actualizar todo lo relacionado a productos

@api_view(['PUT'])
def actualizarCategoria(request, id):
    try:
        categoria = Categoria.objects.get(id=id)
    except Categoria.DoesNotExist:
        return Response({'Error': 'Categoria no encontrada'}, status=404)
    
    serializer = CategoriaSerializer(categoria, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def actualizarProducto(request, id):
    try:
        producto = Producto.objects.get(id=id)
    except Producto.DoesNotExist:
        return Response({'Error': 'Producto no encontrado'}, status=404)
    
    serializer = ProductoSerializer(producto, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def actualizarMarca(request, id):
    try:
        marca = Marca.objects.get(id=id)
    except Marca.DoesNotExist:
        return Response({'Error': 'Marca no encontrada'}, status=404)
    
    serializer = MarcaSerializer(marca, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


# Eliminar todo lo relacionado a productos

@api_view(['GET'])
def eliminarProducto(request, id):
    try:
        producto = Producto.objects.get(id=id)
    except Producto.DoesNotExist:
        return Response({'Error': 'Producto no encontrado'}, status=404)
    
    serializer = ProductoSerializer(producto)
    producto.delete()
    return Response({'Mensaje': 'Producto eliminado', 'producto': serializer.data}, status=200)

@api_view(['GET'])
def eliminarMarca(request, id):
    try:
        marca = Marca.objects.get(id=id)
    except Marca.DoesNotExist:
        return Response({'Error': 'Marca no encontrado'}, status=404)
    
    serializer = MarcaSerializer(marca)
    marca.delete()
    return Response({'Mensaje': 'Marca eliminada', 'Marca': serializer.data}, status=200)

@api_view(['GET'])
def eliminarCategoria(request, id):
    try:
        categoria = Categoria.objects.get(id=id)
    except Categoria.DoesNotExist:
        return Response({'Error': 'Categoría no encontrada'}, status=404)

    serializer = CategoriaSerializer(categoria)
    categoria.delete()
    return Response({'Mensaje': 'Categoría eliminada', 'Categoría': serializer.data}, status=200)


# Vistas para ProductoEspecial

@api_view(['GET'])
def obtenerProductosEspeciales(request):
    productos = ProductoEspecial.objects.all()
    serializer = ProductoEspecialSerializer(productos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def obtenerProductoEspecial(request, id):
    try:
        producto = ProductoEspecial.objects.get(id=id)
    except ProductoEspecial.DoesNotExist:
        return Response({'Error': 'Producto especial no encontrado'}, status=404)
    serializer = ProductoEspecialSerializer(producto)
    return Response(serializer.data)

@api_view(['POST'])
def crearProductoEspecial(request):
    serializer = ProductoEspecialSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=400)

@api_view(['PUT'])
def actualizarProductoEspecial(request, id):
    try:
        producto = ProductoEspecial.objects.get(id=id)
    except ProductoEspecial.DoesNotExist:
        return Response({'Error': 'Producto especial no encontrado'}, status=404)

    serializer = ProductoEspecialSerializer(producto, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def eliminarProductoEspecial(request, id):
    try:
        producto = ProductoEspecial.objects.get(id=id)
    except ProductoEspecial.DoesNotExist:
        return Response({'Error': 'Producto especial no encontrado'}, status=404)

    serializer = ProductoEspecialSerializer(producto)
    producto.delete()
    return Response({'Mensaje': 'Producto especial eliminado', 'producto': serializer.data}, status=200)

@api_view(['POST'])
def calcularPrecioCorte(request):
    id = request.data.get('id')
    ancho_corte = request.data.get('ancho_corte')
    alto_corte = request.data.get('alto_corte')

    if not all([id, ancho_corte, alto_corte]):
        return Response({'Error': 'Faltan parámetros: id, ancho_corte, alto_corte'}, status=400)

    try:
        producto = ProductoEspecial.objects.get(id=id)
    except ProductoEspecial.DoesNotExist:
        return Response({'Error': 'Producto especial no encontrado'}, status=404)

    try:
        ancho_corte = float(ancho_corte)
        alto_corte = float(alto_corte)
    except ValueError:
        return Response({'Error': 'ancho_corte y alto_corte deben ser números'}, status=400)

    precio = producto.calcular_precio_corte(ancho_corte, alto_corte)
    return Response({'precio_corte': precio})


# Vistas para ProductoServicio

@api_view(['GET'])
def obtenerProductosServicio(request):
    productos = ProductoServicio.objects.all()
    serializer = ProductoServicioSerializer(productos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def obtenerProductoServicio(request, id):
    try:
        producto = ProductoServicio.objects.get(id=id)
    except ProductoServicio.DoesNotExist:
        return Response({'Error': 'Producto servicio no encontrado'}, status=404)
    serializer = ProductoServicioSerializer(producto)
    return Response(serializer.data)

@api_view(['POST'])
def crearProductoServicio(request):
    serializer = ProductoServicioSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=400)

@api_view(['PUT'])
def actualizarProductoServicio(request, id):
    try:
        producto = ProductoServicio.objects.get(id=id)
    except ProductoServicio.DoesNotExist:
        return Response({'Error': 'Producto servicio no encontrado'}, status=404)

    serializer = ProductoServicioSerializer(producto, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def eliminarProductoServicio(request, id):
    try:
        producto = ProductoServicio.objects.get(id=id)
    except ProductoServicio.DoesNotExist:
        return Response({'Error': 'Producto servicio no encontrado'}, status=404)

    serializer = ProductoServicioSerializer(producto)
    producto.delete()
    return Response({'Mensaje': 'Producto servicio eliminado', 'producto': serializer.data}, status=200)
