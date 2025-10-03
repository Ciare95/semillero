from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Cliente

class ClienteSerielizer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nombre', 'numero_documento', 'estado']
        
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_active']