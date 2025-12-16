# backend/api/serializers.py
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import ReporteCrimen
from rest_framework import serializers

class ReporteCrimenSerializer(GeoFeatureModelSerializer):
    """
    Serializador que convierte el modelo ReporteCrimen a GeoJSON (para el mapa)
    """
    # Usaremos el campo 'ubicacion' como el campo de geometría principal
    class Meta:
        model = ReporteCrimen
        geo_field = "ubicacion"
        # Asegúrate de incluir todos los campos que el frontend necesita
        fields = (
            'id', 
            'tipo_crimen', 
            'fecha_hora', 
            'descripcion', 
            'ciudad', 
            'estado_verificacion'
        )
        read_only_fields = ('fecha_hora', 'estado_verificacion')
