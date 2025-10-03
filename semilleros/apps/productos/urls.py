from django.urls import path
from . import view_productos

app_name = 'productos'

urlpatterns = [
    # Obtener o mostrar todo lo relacionado a productos
    path('productos', view_productos.obtenerProductos, name='obtener_productos'),
    path('productos/<int:id>/', view_productos.obtenerProducto, name='obtener_producto'),
    path('marcas', view_productos.obtenerMarcas, name='obtener_marcas'),
    path('categorias', view_productos.obtenerCategorias, name='obtener_categorias'),
    
    # Crear todo lo relacionado a productos
    path('crear_producto', view_productos.crearProducto, name="crear_producto"),
    path('crear_categoria', view_productos.crearCategoria, name='crear_categoria'),
    path('crear_marca', view_productos.crearMarca, name='crear_marca'),
    
    # Actualizar todo lo relacionado a produtos
    path('actualizar_categoria/<int:id>', view_productos.actualizarCategoria, name='actualizar_categoria'),
    path('actualizar_marca/<int:id>', view_productos.actualizarMarca, name='actualizar_marca'),
    path('actualizar_producto/<int:id>', view_productos.actualizarProducto, name='actualizar_producto'),
    
    # Eliminar todo lo relacionado a productos
    path('eliminar_producto/<int:id>', view_productos.eliminarProducto, name='eliminar_producto'),
    path('eliminar_categoria/<int:id>', view_productos.eliminarCategoria, name='eliminar_categoria'),
    path('eliminar_marca/<int:id>', view_productos.eliminarMarca, name='eliminar_marca'),

    # ProductoEspecial
    path('productos_especiales', view_productos.obtenerProductosEspeciales, name='obtener_productos_especiales'),
    path('productos_especiales/<int:id>/', view_productos.obtenerProductoEspecial, name='obtener_producto_especial'),
    path('crear_producto_especial', view_productos.crearProductoEspecial, name='crear_producto_especial'),
    path('actualizar_producto_especial/<int:id>', view_productos.actualizarProductoEspecial, name='actualizar_producto_especial'),
    path('eliminar_producto_especial/<int:id>', view_productos.eliminarProductoEspecial, name='eliminar_producto_especial'),
    path('calcular_precio_corte', view_productos.calcularPrecioCorte, name='calcular_precio_corte'),

    # ProductoServicio
    path('productos_servicio', view_productos.obtenerProductosServicio, name='obtener_productos_servicio'),
    path('productos_servicio/<int:id>/', view_productos.obtenerProductoServicio, name='obtener_producto_servicio'),
    path('crear_producto_servicio', view_productos.crearProductoServicio, name='crear_producto_servicio'),
    path('actualizar_producto_servicio/<int:id>', view_productos.actualizarProductoServicio, name='actualizar_producto_servicio'),
    path('eliminar_producto_servicio/<int:id>', view_productos.eliminarProductoServicio, name='eliminar_producto_servicio'),
]
