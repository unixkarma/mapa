# backend/api/urls.py
from rest_framework.routers import DefaultRouter
from .views import ReporteCrimenViewSet

router = DefaultRouter()
# Registra el ViewSet. La URL será: /reportes/
router.register(r'reportes', ReporteCrimenViewSet)

urlpatterns = router.urls
