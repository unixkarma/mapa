# backend/api/views.py
from rest_framework import viewsets
from .models import ReporteCrimen
from .serializers import ReporteCrimenSerializer

class ReporteCrimenViewSet(viewsets.ModelViewSet):
    """
    ViewSet que proporciona las operaciones CRUD (Crear, Leer, Actualizar, Borrar)
    para el modelo ReporteCrimen.
    """
    # Consulta base: solo crímenes verificados
    queryset = ReporteCrimen.objects.filter(estado_verificacion='verificado').order_by('-fecha_hora')
    serializer_class = ReporteCrimenSerializer
    
    # Si quieres que el usuario pueda crear un reporte (POST) aunque no esté verificado:
    # Debes sobrescribir la función perform_create o cambiar el queryset. 
    # Para empezar, mantenemos simple para que solo muestre verificados, pero acepta nuevos.
