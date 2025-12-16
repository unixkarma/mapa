# 🇪🇨 Mapa de Seguridad - Ecuador

Plataforma interactiva de visualización y reporte de incidentes de seguridad en Ecuador. Este proyecto busca crear conciencia sobre la situación de violencia en el país mediante datos verificados de la comunidad.

![Estado](https://img.shields.io/badge/estado-activo-success)
![Frontend](https://img.shields.io/badge/frontend-Next.js-black)
![Backend](https://img.shields.io/badge/backend-Supabase-green)
![Base de Datos](https://img.shields.io/badge/database-PostgreSQL%20%2B%20PostGIS-blue)

## 🎯 Características

✅ **Visualización Interactiva** - Mapa de Ecuador con reportes georreferenciados
✅ **Reportes Comunitarios** - Los ciudadanos pueden reportar incidentes
✅ **Verificación de Reportes** - Sistema de validación antes de publicar
✅ **Actualizaciones en Tiempo Real** - El mapa se actualiza automáticamente
✅ **Estadísticas Dinámicas** - Panel con totales por tipo de crimen
✅ **Diseño Responsivo** - Funciona en móvil, tablet y escritorio
✅ **Código Abierto** - Disponible para la comunidad

## 🛠️ Stack Tecnológico

### Frontend
- **Next.js 16** - Framework React con SSR
- **React 19** - Biblioteca de interfaces
- **Tailwind CSS 4** - Framework de estilos
- **Leaflet** - Mapas interactivos
- **React Leaflet** - Integración de Leaflet con React
- **Supabase JS Client** - Cliente para el backend

### Backend
- **Supabase** - Backend como servicio (BaaS)
- **PostgreSQL** - Base de datos relacional
- **PostGIS** - Extensión geoespacial de PostgreSQL
- **Row Level Security (RLS)** - Seguridad a nivel de filas

## 📁 Estructura del Proyecto

```
Mapa/
├── backend/          # [DEPRECADO] Backend Django anterior
├── frontend/         # Aplicación Next.js
│   ├── src/
│   │   ├── app/          # Rutas y layouts de Next.js
│   │   ├── components/   # Componentes React
│   │   ├── lib/          # Configuración (Supabase)
│   │   └── services/     # Servicios (crimeService)
│   ├── public/           # Archivos estáticos
│   ├── supabase-schema.sql  # Script SQL para Supabase
│   ├── SUPABASE_SETUP.md    # Guía de configuración
│   └── package.json
└── README.md         # Este archivo
```

## 🚀 Instalación y Configuración

### Paso 1: Clonar el Repositorio

```bash
git clone <tu-repositorio>
cd Mapa/frontend
```

### Paso 2: Instalar Dependencias

```bash
npm install
```

### Paso 3: Configurar Supabase

**Lee la guía completa:** [`frontend/SUPABASE_SETUP.md`](./frontend/SUPABASE_SETUP.md)

**Resumen rápido:**

1. Crea un proyecto en [Supabase](https://supabase.com)
2. Ejecuta el script SQL en `frontend/supabase-schema.sql`
3. Copia tus credenciales:
   - Project URL
   - Anon/Public Key
4. Crea `frontend/.env.local`:

```env
NEXT_PUBLIC_SUPABASE_URL=https://tu-proyecto.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=tu_anon_key_aqui
```

### Paso 4: Ejecutar la Aplicación

```bash
npm run dev
```

Abre [http://localhost:3000](http://localhost:3000) en tu navegador.

## 📊 Tipos de Crímenes Soportados

El sistema actualmente soporta los siguientes tipos de incidentes:

- 🔴 **Homicidio** - Incidentes fatales
- 🟠 **Robo** - Robos a mano armada, asaltos, hurtos
- 🟣 **Violencia Intrafamiliar** - Violencia doméstica
- 🔵 **Otro** - Otros tipos de incidentes

## 🔒 Seguridad y Privacidad

- **Verificación Manual**: Los reportes no aparecen inmediatamente en el mapa
- **Row Level Security**: Políticas de seguridad a nivel de base de datos
- **Sin Datos Personales**: No se solicita información personal identificable
- **Geolocalización Opcional**: El usuario elige manualmente la ubicación

## 🎨 Capturas de Pantalla

### Mapa Principal
![Mapa](docs/screenshot-mapa.png)

### Formulario de Reporte
![Formulario](docs/screenshot-form.png)

### Estadísticas
![Estadísticas](docs/screenshot-stats.png)

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Este es un proyecto comunitario.

### Formas de Contribuir

1. **Reportar Bugs** - Abre un issue describiendo el problema
2. **Sugerir Features** - Comparte ideas para mejorar la plataforma
3. **Mejorar Documentación** - Ayuda a otros a entender el proyecto
4. **Código** - Envía pull requests con mejoras

### Proceso de Contribución

1. Fork el repositorio
2. Crea una rama: `git checkout -b feature/nueva-funcionalidad`
3. Haz tus cambios y commit: `git commit -m 'Agregar nueva funcionalidad'`
4. Push a tu fork: `git push origin feature/nueva-funcionalidad`
5. Abre un Pull Request

## 📝 Roadmap

### Completado ✅
- [x] Migración de Django a Supabase
- [x] Visualización de reportes en mapa
- [x] Formulario de reporte de incidentes
- [x] Sistema de verificación
- [x] Estadísticas dinámicas
- [x] Actualizaciones en tiempo real
- [x] Diseño responsivo

### En Proceso 🚧
- [ ] Panel de administración
- [ ] Sistema de autenticación
- [ ] Filtros por fecha, tipo, ciudad

### Futuro 🔮
- [ ] Mapas de calor
- [ ] Notificaciones por zona
- [ ] API pública
- [ ] Aplicación móvil nativa
- [ ] Exportar datos (CSV, Excel)
- [ ] Análisis de tendencias
- [ ] Integración con datos oficiales

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 🙏 Agradecimientos

- A la comunidad de Ecuador por su apoyo
- A los contribuidores del proyecto
- A [Supabase](https://supabase.com) por su excelente plataforma
- A [OpenStreetMap](https://www.openstreetmap.org) por los mapas

## 📞 Contacto

Para preguntas o sugerencias sobre el proyecto:

- Abre un [Issue](../../issues)
- Contribuye con un [Pull Request](../../pulls)

---

**Nota**: Este proyecto es una iniciativa comunitaria para crear conciencia sobre la seguridad en Ecuador. Los datos mostrados son reportes de la comunidad y están sujetos a verificación.

🇪🇨 **Hecho con ❤️ para Ecuador**
