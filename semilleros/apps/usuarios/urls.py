from django.urls import path
from . import view

app_name = 'usuarios'

urlpatterns = [
    # Obtener todo lo relacionado a usuarios
    path('usuarios', view.obtenerUsuarios, name='obtener_usuarios'),
    path('clientes', view.obtenerClientes, name='obtener_clientes'),
    
    # Crear todo lo relacionado a usuarios
    path('crear_cliente', view.crearCliente, name='crear_cliente'),
    path('crear_usuario', view.crearUsuario, name='crear_usuario'),
    
    # Actualizar todo lo relacionado a usuarios
    path('actualizar_cliente/<id>', view.actualizarCliente, name='actualizar_cliente'),
    path('actualizar_usuario/<id>', view.actualizarUsuarios, name='actualizar_usuarios'),
    
    #Eliminar todo lo relacionado a usuarios
    path('eliminar_cliente/<id>', view.eliminarCliente, name='eliminar_cliente'),
    path('eliminar_usuario/<id>', view.eliminarUsuario, name='eliminar_usuario'),
]