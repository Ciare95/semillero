from django.urls import path
from . import view_compras

app_name = 'compras'

urlpatterns = [
    # Proveedores
    path('proveedores', view_compras.obtenerProveedores, name='obtener_proveedores'),
    path('crear_proveedor', view_compras.crearProveedor, name='crear_proveedor'),
    path('actualizar_proveedor/<int:id>', view_compras.actualizarProveedor, name='actualizar_proveedor'),
    path('eliminar_proveedor/<int:id>', view_compras.eliminarProveedor, name='eliminar_proveedor'),

    # Facturas Compra
    path('facturas_compra', view_compras.obtenerFacturasCompra, name='obtener_facturas_compra'),
    path('factura_compra/<int:id>', view_compras.obtenerFacturaCompra, name='obtener_factura_compra'),
    path('crear_factura_compra', view_compras.crearFacturaCompra, name='crear_factura_compra'),
    path('actualizar_factura_compra/<int:id>', view_compras.actualizarFacturaCompra, name='actualizar_factura_compra'),
    path('eliminar_factura_compra/<int:id>', view_compras.eliminarFacturaCompra, name='eliminar_factura_compra'),

    # Gastos
    path('gastos', view_compras.obtenerGastos, name='obtener_gastos'),
    path('crear_gasto', view_compras.crearGasto, name='crear_gasto'),
    path('actualizar_gasto/<int:id>', view_compras.actualizarGasto, name='actualizar_gasto'),
    path('eliminar_gasto/<int:id>', view_compras.eliminarGasto, name='eliminar_gasto'),
]