from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Cliente, User
from .serializers import ClienteSerielizer, UsuarioSerializer


# Funciones para obtener elementos relacionados a usuarios

@api_view(['GET'])
def obtenerUsuarios(request):
    usuario = User.objects.all()
    serializer = UsuarioSerializer(usuario, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def obtenerClientes(request):
    cliente = Cliente.objects.all()
    serializer = ClienteSerielizer(cliente, many=True)
    return Response(serializer.data)


# Funciones para crear elementos relacionados a usuarios

@api_view(['POST'])
def crearCliente(request):
    serializer = ClienteSerielizer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=400)
    
@api_view(['POST'])
def crearUsuario(request):
    serializer = UsuarioSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=400)
    

# Funciones para actualizar elementos relacionados a usuarios

@api_view(['PUT'])
def actualizarCliente(request, id):
    try:
        cliente = Cliente.objects.get(id=id)
    except Cliente.DoesNotExist:
        return Response({'Error': 'Cliente no encontrado'}, status=404)
    
    serializer = ClienteSerielizer(cliente, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def actualizarUsuarios(request, id):
    try:
        usuario = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response({'Error': 'El usuario no existe'}, status=404)
    
    serializer = UsuarioSerializer(usuario, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def eliminarCliente(request, id):
    try:
        cliente = Cliente.objects.get(id=id)
    except Cliente.DoesNotExist:
        return Response({'Error': 'El cliente no existe'}, status=404)
    
    serializer = ClienteSerielizer(cliente)
    cliente.delete()
    return Response({'Mensaje': 'Cliente eliminado', 'Cliente': serializer.data}, status=200)
    
@api_view(['GET'])
def eliminarUsuario(request, id):
    try:
        usuario = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response({'Error': 'Usuario no existe'})
    
    serializer = UsuarioSerializer(usuario)
    usuario.save()
    return Response({'Mensaje': 'Usuario eliminado', 'Usuario': serializer.data}, status=200)