# Mapa de Delitos - CTM El Risco

## Descripción

Este proyecto es una visualización interactiva de delitos en la zona de CTM El Risco utilizando un mapa web. La aplicación muestra la distribución geográfica de diferentes tipos de delitos mediante círculos de diferentes tamaños y colores, proporcionando una representación visual clara de la incidencia delictiva en la zona.

## Características

### 🗺️ Visualización Interactiva
- **Mapa base**: Utiliza OpenStreetMap para mostrar el contexto geográfico
- **Polígono de área**: Delimita exactamente la zona de CTM El Risco
- **Círculos proporcionales**: El tamaño de cada círculo representa la cantidad de delitos
- **Colores distintivos**: Cada tipo de delito tiene un color único para fácil identificación

### 📊 Datos de Delitos
El mapa incluye los siguientes tipos de delitos con sus respectivas cantidades:

| Tipo de Delito | Cantidad | Porcentaje |
|----------------|----------|------------|
| Violencia Familiar | 31 | 29.8% |
| Robo | 19 | 18.3% |
| Amenazas | 12 | 11.5% |
| Daño A La Propiedad | 7 | 6.7% |
| Fraude | 6 | 5.8% |
| Usurpación | 4 | 3.8% |
| Abuso De Autoridad | 3 | 2.9% |
| Tentativa | 3 | 2.9% |
| Electorales | 2 | 1.9% |
| Lesiones Culposas | 2 | 1.9% |
| Despojo | 2 | 1.9% |
| Allanamiento | 1 | 1.0% |
| Contra La Intimidad Sexual | 1 | 1.0% |
| Corrupción De Menores | 1 | 1.0% |
| Encubrimiento | 1 | 1.0% |
| Ambiental | 1 | 1.0% |
| Narcomenudeo | 1 | 1.0% |

**Total de delitos: 104**

### 🎛️ Controles y Funcionalidades
- **Leyenda interactiva**: Muestra todos los tipos de delitos con colores y porcentajes
- **Contador total**: Displays el número total de delitos registrados
- **Botón centrar**: Permite volver a la vista completa del área
- **Popups informativos**: Al hacer clic en cada círculo se muestra información detallada

## Tecnologías Utilizadas

### Frontend
- **HTML5**: Estructura de la página
- **CSS3**: Estilos y diseño responsivo
- **JavaScript ES6**: Lógica de la aplicación

### Librerías
- **Leaflet 1.7.1**: Biblioteca principal para mapas interactivos
- **Turf.js 6.0**: Análisis geoespacial y cálculos geométricos
- **OpenStreetMap**: Proveedor de tiles del mapa base

## Algoritmos Implementados

### 🎯 Distribución Inteligente de Círculos
El sistema utiliza un algoritmo sofisticado para distribuir los círculos de delitos:

1. **Cálculo de área**: Determina el área total del polígono de CTM El Risco
2. **Distribución en grilla**: Crea una grilla inicial basada en el aspect ratio del área
3. **Validación geográfica**: Verifica que todos los puntos estén dentro del polígono
4. **Optimización de distancias**: Utiliza un algoritmo greedy para maximizar la separación entre círculos
5. **Ajuste de tamaños**: Calcula radios proporcionales basados en la cantidad de delitos

### 📐 Cálculos Geométricos
- **Centro del polígono**: Utiliza Turf.js para calcular el centroide geométrico
- **Área del polígono**: Calcula el área en metros cuadrados para dimensionar círculos
- **Distancias mínimas**: Evita superposiciones excesivas entre círculos
- **Validación de límites**: Asegura que los círculos se mantengan dentro del área definida

## Estructura del Proyecto

```
├── mapa-delitos-distribuidos.html    # Archivo principal de la aplicación
├── README.md                         # Documentación del proyecto
└── assets/                          # (Opcional) Carpeta para recursos adicionales
```

## Instalación y Uso

### Requisitos
- Navegador web moderno (Chrome, Firefox, Safari, Edge)
- Conexión a internet (para cargar las librerías CDN y tiles del mapa)

### Ejecución
1. Descarga el archivo `mapa-delitos-distribuidos.html`
2. Abre el archivo en tu navegador web
3. El mapa se cargará automáticamente mostrando la visualización de delitos

### Uso de la Interfaz
- **Navegación**: Usa el mouse para hacer zoom y pan en el mapa
- **Información**: Haz clic en cualquier círculo para ver detalles del delito
- **Centrar**: Usa el botón "Centrar Mapa" para volver a la vista completa
- **Leyenda**: Consulta la leyenda en la esquina inferior izquierda para identificar tipos de delitos

## Configuración Avanzada

### Modificar Datos de Delitos
Para actualizar los datos de delitos, modifica el array `delitos` en el JavaScript:

```javascript
const delitos = [
  { nombre: "Nuevo Delito", cantidad: 5 },
  // ... más delitos
];
```

### Cambiar Área Geográfica
Para cambiar el polígono del área, modifica las coordenadas en `poligonoElRisco`:

```javascript
const poligonoElRisco = {
  "type": "Feature",
  "geometry": {
    "type": "Polygon",
    "coordinates": [[
      // Nuevas coordenadas [longitud, latitud]
    ]]
  }
};
```

### Personalizar Colores
Modifica el array `colores` para cambiar la paleta de colores:

```javascript
const colores = [
  '#e41a1c', '#377eb8', '#4daf4a', // ... más colores
];
```

## Características Técnicas

### Rendimiento
- **Carga rápida**: Utiliza CDNs para librerías externas
- **Optimización de memoria**: Algoritmos eficientes para cálculos geométricos
- **Responsivo**: Se adapta a diferentes tamaños de pantalla

### Compatibilidad
- **Navegadores**: Compatible con todos los navegadores modernos
- **Dispositivos**: Funciona en desktop, tablet y móvil
- **Resoluciones**: Diseño responsivo para diferentes resoluciones

## Contribuciones

Para contribuir al proyecto:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crea un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## Contacto

Para preguntas o sugerencias sobre este proyecto, por favor contacta al equipo de desarrollo.

---

**Nota**: Este mapa es una herramienta de visualización con fines informativos y de análisis. Los datos mostrados corresponden a registros oficiales de delitos en la zona de CTM El Risco.
