from django.urls import path
from . import view_inventario

app_name = 'inventario'

urlpatterns = [
    # Secciones
    path('secciones', view_inventario.obtenerSecciones, name='obtener_secciones'),
    path('crear_seccion', view_inventario.crearSeccion, name='crear_seccion'),
    path('actualizar_seccion/<int:id>', view_inventario.actualizarSeccion, name='actualizar_seccion'),
    path('eliminar_seccion/<int:id>', view_inventario.eliminarSeccion, name='eliminar_seccion'),

    # Ubicaciones
    path('ubicaciones', view_inventario.obtenerUbicaciones, name='obtener_ubicaciones'),
    path('crear_ubicacion', view_inventario.crearUbicacion, name='crear_ubicacion'),
    path('actualizar_ubicacion/<int:id>', view_inventario.actualizarUbicacion, name='actualizar_ubicacion'),
    path('eliminar_ubicacion/<int:id>', view_inventario.eliminarUbicacion, name='eliminar_ubicacion'),

    # Categorias Inventario
    path('categorias_inventario', view_inventario.obtenerCategoriasInventario, name='obtener_categorias_inventario'),
    path('crear_categoria_inventario', view_inventario.crearCategoriaInventario, name='crear_categoria_inventario'),
    path('actualizar_categoria_inventario/<int:id>', view_inventario.actualizarCategoriaInventario, name='actualizar_categoria_inventario'),
    path('eliminar_categoria_inventario/<int:id>', view_inventario.eliminarCategoriaInventario, name='eliminar_categoria_inventario'),

    # Subcategorias Inventario
    path('subcategorias_inventario', view_inventario.obtenerSubcategoriasInventario, name='obtener_subcategorias_inventario'),
    path('crear_subcategoria_inventario', view_inventario.crearSubcategoriaInventario, name='crear_subcategoria_inventario'),
    path('actualizar_subcategoria_inventario/<int:id>', view_inventario.actualizarSubcategoriaInventario, name='actualizar_subcategoria_inventario'),
    path('eliminar_subcategoria_inventario/<int:id>', view_inventario.eliminarSubcategoriaInventario, name='eliminar_subcategoria_inventario'),

    # Inventario Items
    path('inventario_items', view_inventario.obtenerInventarioItems, name='obtener_inventario_items'),
    path('crear_inventario_item', view_inventario.crearInventarioItem, name='crear_inventario_item'),
    path('actualizar_inventario_item/<int:id>', view_inventario.actualizarInventarioItem, name='actualizar_inventario_item'),
    path('eliminar_inventario_item/<int:id>', view_inventario.eliminarInventarioItem, name='eliminar_inventario_item'),

    # Vista especial
    path('inventario_por_categoria', view_inventario.obtenerInventarioPorCategoria, name='inventario_por_categoria'),
]