from django.urls import path
from .view_ventas import listarVentas, obtener_venta, crearVenta, anularVenta

urlpatterns = [
    # Listar ventas (GET)
    path('listar_ventas/', listarVentas, name='listar_ventas'),
    # Obtener una venta por ID (GET)
    path('obtener_venta/<int:id>/', obtener_venta, name='obtener_venta'),
    # Crear venta (POST)
    path('crear_venta/', crearVenta, name='crear_venta'),
    # Anular venta por ID (GET)
    path('anular_venta/<int:id>/', anularVenta, name='anular_venta'),
]
