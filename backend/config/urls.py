# backend/config/urls.py
from django.contrib import admin
from django.urls import path, include
# Importa las URLs que acabamos de crear en la app 'api'
from api import urls as api_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    # Agrega el endpoint principal de la API
    # El frontend accederá a la API en: http://127.0.0.1:8000/api/v1/reportes/
    path('api/v1/', include(api_urls)), 
]
