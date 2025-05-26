# Sistema de Análisis Geoespacial de Delitos - CTM El Risco

## 📋 Descripción General

Este proyecto es un **sistema integral de análisis geoespacial** que proporciona múltiples herramientas de visualización y análisis de datos delictivos en la zona de CTM El Risco. La aplicación ha evolucionado de un simple mapa de delitos a una plataforma completa con diferentes módulos especializados para el análisis criminológico y geográfico.

## 🏗️ Arquitectura del Sistema

El sistema está organizado en módulos independientes, cada uno especializado en un tipo específico de análisis:

```
📁 Sistema de Análisis Geoespacial/
├── 📄 index.html                    # Módulo principal - Mapa interactivo con filtros avanzados
├── 📁 zona_riesgo/                  # Análisis de zonas de riesgo con polígonos
├── 📁 hot_spot/                     # Análisis de puntos calientes (Hot Spots)
├── 📁 concentricos_burgues/         # Modelo de Burgess - Círculos concéntricos
├── 📁 cartografia/                  # Visualización cartográfica básica
├── 📁 ProcesamientoDatos/           # Scripts y datos procesados
└── 📄 README.md                     # Documentación del sistema
```

## 🚀 Módulos del Sistema

### 1. 🗺️ **Módulo Principal** (`index.html`)
**Mapa interactivo con sistema de filtros avanzados**

#### Características:
- **Visualización de 2,800+ delitos** con datos reales georeferenciados
- **Sistema de filtros inteligente** con chips interactivos
- **Filtros por tipo de delito** con selección múltiple
- **Filtros temporales** (año, mes, día de la semana, hora)
- **Estadísticas en tiempo real** que se actualizan con los filtros
- **Interfaz responsive** optimizada para móviles y desktop
- **Mapa base OpenStreetMap** con controles de navegación

#### Funcionalidades Avanzadas:
- Filtrado maestro por categorías de delitos
- Visualización de estadísticas dinámicas
- Sistema de notificaciones para resultados de filtros
- Optimización de rendimiento para grandes volúmenes de datos

### 2. 🎯 **Módulo de Zonas de Riesgo** (`zona_riesgo/`)
**Análisis territorial con polígonos de riesgo**

#### Características:
- **Polígonos de zonas** con diferentes niveles de riesgo
- **Clasificación por intensidad** de actividad delictiva
- **Filtros especializados** para análisis territorial
- **Visualización por densidad** de delitos por zona
- **Análisis comparativo** entre diferentes áreas

#### Datos Incluidos:
- Archivo `poligonos_zonas.js` con geometrías de zonas
- Archivo `delitos_data.js` con datos procesados
- Sistema de colores por nivel de riesgo

### 3. 🔥 **Módulo Hot Spots** (`hot_spot/`)
**Identificación de puntos calientes de actividad delictiva**

#### Características:
- **Análisis de concentración** de delitos por área
- **Identificación automática** de puntos calientes
- **Visualización por intensidad** con gradientes de color
- **Análisis temporal** de evolución de hot spots
- **Métricas de densidad** delictiva

### 4. 🎯 **Módulo Círculos Concéntricos** (`concentricos_burgues/`)
**Implementación del Modelo de Burgess para análisis urbano**

#### Características:
- **Modelo teórico de Burgess** aplicado a datos reales
- **Círculos concéntricos** desde el centro urbano
- **Análisis por distancia** del centro de la ciudad
- **Comparación de patrones** delictivos por zona concéntrica
- **Controles interactivos** para ajustar parámetros del modelo

#### Funcionalidades:
- Generación automática de círculos concéntricos
- Análisis de distribución delictiva por anillo
- Visualización de patrones urbanos
- Controles para modificar radio y número de círculos

### 5. 🗺️ **Módulo de Cartografía** (`cartografia/`)
**Visualización cartográfica básica y polígonos**

#### Características:
- **Visualización simple** de polígonos geográficos
- **Interfaz minimalista** para análisis básico
- **Leyenda interactiva** con colores por zona
- **Controles básicos** de navegación

### 6. 🔧 **Módulo de Procesamiento** (`ProcesamientoDatos/`)
**Scripts y herramientas para procesamiento de datos**

#### Contenido:
- **`index.py`**: Script de Python para conversión Excel → JSON
- **`delitos.xlsx`**: Datos originales en formato Excel (2,800+ registros)
- **`delitos.json`**: Datos en formato JSON sin procesar
- **`delitos_procesados.json`**: Datos limpios y estructurados

#### Funcionalidades del Script:
- Conversión automática de Excel a JSON
- Limpieza y estructuración de datos
- Manejo de caracteres especiales
- Extracción de campos relevantes (tipo, fecha, hora, coordenadas)

## 📊 Datos del Sistema

### Volumen de Información
- **Total de delitos**: 2,800+ registros georeferenciados
- **Tipos de delitos**: 17+ categorías diferentes
- **Cobertura temporal**: Datos históricos con fechas y horas
- **Precisión geográfica**: Coordenadas exactas (lat/lng)

### Principales Tipos de Delitos
| Tipo de Delito | Frecuencia | Análisis |
|----------------|------------|----------|
| Violencia Familiar | Alta | Patrón residencial |
| Robo | Alta | Concentrado en zonas comerciales |
| Amenazas | Media | Distribuido uniformemente |
| Daño a la Propiedad | Media | Relacionado con vandalismo |
| Fraude | Media | Concentrado en centros urbanos |
| Otros | Variable | Patrones específicos por tipo |

## 🛠️ Tecnologías Utilizadas

### Frontend
- **HTML5**: Estructura semántica y accesible
- **CSS3**: Diseño moderno con gradientes y animaciones
- **JavaScript ES6+**: Lógica avanzada y manipulación de datos
- **Responsive Design**: Optimizado para todos los dispositivos

### Librerías y APIs
- **Leaflet 1.7.1**: Mapas interactivos de alto rendimiento
- **Turf.js 6.0**: Análisis geoespacial y cálculos geométricos
- **OpenStreetMap**: Tiles de mapa base gratuitos
- **GeoJSON**: Formato estándar para datos geográficos

### Backend/Procesamiento
- **Python 3.x**: Scripts de procesamiento de datos
- **Pandas**: Manipulación y análisis de datos
- **JSON**: Formato de intercambio de datos

## 🚀 Instalación y Configuración

### Requisitos del Sistema
- **Navegador moderno**: Chrome 80+, Firefox 75+, Safari 13+, Edge 80+
- **Conexión a internet**: Para cargar librerías CDN y tiles de mapa
- **Python 3.x**: Solo para procesamiento de datos (opcional)

### Instalación Rápida
1. **Clona o descarga** el repositorio completo
2. **Abre cualquier módulo** directamente en el navegador:
   - `index.html` - Módulo principal
   - `zona_riesgo/index.html` - Análisis de zonas
   - `hot_spot/index.html` - Puntos calientes
   - `concentricos_burgues/index.html` - Modelo de Burgess
   - `cartografia/index.html` - Cartografía básica

### Configuración de Datos (Opcional)
Si necesitas procesar nuevos datos:

```bash
cd ProcesamientoDatos/
python index.py
```

## 📱 Uso del Sistema

### Navegación Entre Módulos
Cada módulo es independiente y se puede usar por separado según el tipo de análisis requerido:

- **Análisis general**: Usar módulo principal
- **Análisis territorial**: Usar módulo de zonas de riesgo
- **Identificación de hot spots**: Usar módulo hot spots
- **Análisis urbano teórico**: Usar módulo de círculos concéntricos
- **Visualización simple**: Usar módulo de cartografía

### Controles Comunes
- **Zoom**: Rueda del mouse o controles táctiles
- **Pan**: Arrastrar el mapa
- **Información**: Clic en elementos para detalles
- **Filtros**: Usar controles específicos de cada módulo
- **Centrar**: Botón para volver a la vista completa

## 🔧 Configuración Avanzada

### Personalización de Datos
Para actualizar los datos en cualquier módulo:

1. **Modifica el archivo de datos** correspondiente
2. **Mantén la estructura JSON** existente
3. **Actualiza las coordenadas** si cambias la zona de estudio

### Personalización Visual
- **Colores**: Modifica arrays de colores en cada módulo
- **Estilos**: Edita las secciones CSS de cada archivo
- **Tamaños**: Ajusta parámetros de círculos y polígonos

### Extensión del Sistema
Para agregar nuevos módulos:

1. **Crea una nueva carpeta** con estructura similar
2. **Incluye los archivos** HTML, CSS y JS necesarios
3. **Mantén la consistencia** de diseño y funcionalidad
4. **Documenta** las nuevas características

## 📈 Características Técnicas Avanzadas

### Optimización de Rendimiento
- **Carga lazy** de datos grandes
- **Clustering** automático para muchos puntos
- **Debouncing** en filtros para mejor UX
- **Caché** de cálculos geométricos complejos

### Algoritmos Implementados
- **Distribución espacial** inteligente de elementos
- **Cálculo de densidades** por área
- **Análisis de proximidad** entre puntos
- **Generación automática** de polígonos de riesgo
- **Clustering** jerárquico para hot spots

### Compatibilidad y Accesibilidad
- **Responsive design** para todos los dispositivos
- **Controles táctiles** optimizados para móviles
- **Navegación por teclado** en elementos interactivos
- **Colores accesibles** con suficiente contraste

## 🤝 Contribuciones

### Cómo Contribuir
1. **Fork** el repositorio
2. **Crea una rama** para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. **Desarrolla** siguiendo las convenciones del proyecto
4. **Prueba** en diferentes dispositivos y navegadores
5. **Commit** con mensajes descriptivos
6. **Push** y crea un **Pull Request**

### Áreas de Mejora
- **Nuevos algoritmos** de análisis geoespacial
- **Integración** con APIs de datos en tiempo real
- **Exportación** de reportes y análisis
- **Análisis predictivo** con machine learning
- **Integración** con sistemas de información geográfica (SIG)

## 📄 Licencia

Este proyecto está bajo la **Licencia MIT**. Ver el archivo `LICENSE` para más detalles.

## 📞 Contacto y Soporte

Para preguntas, sugerencias o reportes de bugs:
- **Issues**: Usa el sistema de issues del repositorio
- **Documentación**: Consulta este README y comentarios en el código
- **Contribuciones**: Sigue el proceso de Pull Requests

---

## 🎯 Casos de Uso

### Para Analistas de Seguridad
- **Identificación** de patrones delictivos
- **Análisis temporal** de tendencias
- **Evaluación** de efectividad de medidas de seguridad

### Para Planificadores Urbanos
- **Análisis** de distribución espacial del crimen
- **Identificación** de zonas que requieren intervención
- **Planificación** de recursos de seguridad

### Para Investigadores
- **Validación** de teorías criminológicas
- **Análisis** de patrones urbanos
- **Generación** de hipótesis para investigación

### Para Autoridades Locales
- **Toma de decisiones** basada en datos
- **Asignación** eficiente de recursos
- **Comunicación** efectiva con la comunidad

---

**Nota**: Este sistema es una herramienta de análisis con fines informativos, educativos y de investigación. Los datos mostrados corresponden a registros reales de delitos en la zona de CTM El Risco y deben ser utilizados de manera responsable y ética.
