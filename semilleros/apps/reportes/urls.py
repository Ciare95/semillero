from django.urls import path
from . import view_reportes

app_name = 'reportes'

urlpatterns = [
    # Obtener o mostrar todo lo relacionado a reportes
    path('reportes', view_reportes.obtenerReportes, name='obtener_reportes'),

    # Crear todo lo relacionado a reportes
    path('crear_reporte', view_reportes.crearReporte, name='crear_reporte'),

    # Reportes específicos
    path('reporte_ventas', view_reportes.reporteVentas, name='reporte_ventas'),
    path('reporte_productos', view_reportes.reporteProductos, name='reporte_productos'),
    path('reporte_clientes', view_reportes.reporteClientes, name='reporte_clientes'),
    path('ingresos_gastos', view_reportes.ingresosGastos, name='ingresos_gastos'),
]
