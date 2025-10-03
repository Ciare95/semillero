from rest_framework import serializers
from .models import Reporte

class ReporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporte
        fields = ['id', 'titulo', 'tipo', 'descripcion', 'fecha_creacion', 'datos']