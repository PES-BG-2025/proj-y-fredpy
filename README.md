[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/7IRjtlNy)
# Presentación final del curso de Programación I

Este repositorio tiene como propósito servir de contenedor para los archivos de la presentación final del curso. Se deben guardar todos los archivos utilizados para la presentación (vea las condiciones de entrega más adelante). 

*Banco de Guatemala*  
*Maestría en Economía y Finanzas Aplicadas*  
*Programación I*  
*Fecha: Septiembre de 2025*

## Objetivos

El presente proyecto tiene como objetivo que el estudiante conozca nuevos paquetes del lenguaje de Python o que desarrolle lógica de programación necesaria para realizar alguna aplicación interesante utilizando programación científica o métodos de simulación de Monte Carlo. 


## Rúbrica de evaluación 

| Aspecto a evaluar                                                                             |  Punteo |
|:----------------------------------------------------------------------------------------------|--------:|
| Definición y delimitación del proyecto                                                        |      10 |
| El proyecto requiere conocimientos/esfuerzo adicional al ganado/realizado en el curso         |      10 |
| Participantes del grupo colaboraron cada uno con confirmaciones (*commits*) en el repositorio |      10 |
| Exposición clara, interacción con el público y manejo de los límites de tiempo (5-10 minutos) |      20 |
| El proyecto utiliza conceptos, paquetes, algoritmos o herramientas no vistas en clase         |      20 |
| Dominio del código y manejo de preguntas de los estudiantes o del profesor                    |      30 |
| **Total**                                                                                     | **100** |


## Formato de entrega 

- El proyecto debe entregarse utilizando la plataforma de GitHub, a través de las confirmaciones (*commits*) necesarios por los miembros de cada equipo. 
  - Tomar en cuenta que el repositorio será público. Evitar compartir datos personales, contraseñas u otra información sensible. Los repositorios pueden ser visitados nuevamente en el sitio de la organización `PES-BG-2025` para futuras consultas de parte de todos los estudiantes. 
- Los archivos finales del proyecto se pueden guardar en el directorio raíz del repositorio utilizando cualquier estructura deseada. Sin embargo, si se utilizan archivos de prueba que puedan servir como muestra del procedimiento realizado, pero que no formen parte del proyecto final, se deben guardar en un directorio especial denominado `deprecated`. 
- No cargar archivos al repositorio que sean demasiado grandes (>10MB) como fotografías o vídeos. Utilizar recursos o plataformas web específicamente diseñadas para estos propósitos. La única excepción a esta regla es para el archivo de presentación. 
- Un archivo de presentación es opcional. Si se utiliza una presentación en PowerPoint o PDF, esta debe ser adjuntada en la raíz del proyecto. 
- Al final de la presentación, se dará un tiempo para realizar preguntas, tanto del profesor o de los estudiantes.
- Atender a otras indicaciones adicionales por parte del instructor al inicio y durante la presentación. 
- La fecha de entrega máxima para realizar las confirmaciones será el **jueves 25 de septiembre de 2025 a las 23:59 horas**.

- ## Uso de inteligencia artificial

- En cada presentación, los profesores medirán un índice de uso de inteligencia artifical (IA) de 0 a 10 con base en el dominio del código y preguntas que puedan surgir. 
- Si se detecta el uso de ChatGPT o chatbots para realizar partes significativas del código, se aplicará un factor de descuento con base en este índice:

| Índice de uso (0 - 10)    |  % descuento |
|:-------|--------:|
| 0 - 3  |      0% |
| 4 - 6  |     30% |
| 7 - 8  |     60% |
| 9 - 10 |     90% |

**El uso de IA está permitido, pero su mal uso está prohibido.**

- Ejemplos de buen uso:
  - Explicación de piezas de código o sentencias del lenguaje.
  - Depuración de errores.
  - Elaboración de casos de pruebas.
  - Generación de ideas o mejoras en un programa.
  - Elaborar los docstrings de las funciones.
  - Consulta sobre flujos de trabajo en VSCode, GitHub, etc.
  - Pedir ejemplos sobre cómo utilizar una librería en Python. 
 
- Ejemplos de mal uso: 
  - Pedir a los chatbots que elaboren funciones o clases completas.
  - No entender el código brindado por los chatbots (uso ciego).
  - No entender la organización del código porque todo fue elaborado por el chatbot.


------------------------------------------------------
-----------------------------------------------------
# FREDpy (Dashboard de variables macroeconómicas de EE.UU.)
## “Indicadores Externos y Actividad Económica con FRED: Exportaciones, Importaciones y PNB”

## 1) Resumen
El proyecto consiste en un **pipeline de datos en Python** para consultar la API de **FRED** (Federal Reserve Bank of St. Louis), obtener **series temporales de Exportaciones, Importaciones y PNB** de EE. UU., y producir:
1) **Gráficas comparables** (niveles y tasas de variación),
2) Un **dashboard interactivo** (Dash) para explorar periodos.

El resultado permitirá analizar la relación entre el sector externo y la actividad económica de forma reproducible y extensible.

---

## 2) Objetivos
- **O1.** Consumir la API de FRED de forma programática y robusta (módulo Python reusable).
- **O2.** Estandarizar y documentar el **proceso ETL** (extracción, transformación y carga).
- **O3.** Generar **visualizaciones** y un **dashboard** con filtros por rango de fechas (variación trimestral).

- **O4.** utilización de las librerios `dash` para el dashboard y `requests` para consumir API de la FRED
---

## 3) Alcance y Entregables
- **PNB** (trimestral).
- **Exportaciones de Bienes y Servicios** (trimestral).
- **Importaciones de Bienes y Servicios** (trimestral).

**Nota:** Las IDs exactas de FRED se parametrizarán. Evitamos hardcodear IDs para facilitar mantenimiento.

---

## 4) Metodología y Arquitectura

- **Autenticación:** API Key de FRED `config.toml`.
- **Frecuencias:** Trimestral
- **Transformaciones:** 
  - **Δ% trimestral (QoQ)**
---

## 5) Endpoints de FRED a utilizar (plan)
- **Búsqueda de series:** `GET /fred/series/series`  
  - Obtener información para el uso de indices “Exports of Goods and Services”, “Imports of Goods and Services” y "Real Gross National Product".
- **Datos de series:** `GET /fred/series/observations`  
  <!-- - Parámetros: `series_id`, `observation_start`, `observation_end`, `frequency`, `aggregation_method`, `output_type`. -->
  Parámetros: `series_id`, `observation_start`, `observation_end`, `output_type`.
<!-- 
> Se implementarán **funciones wrapper**:  
> `search_series(query, limit=5)`, `get_series(series_id, params)`, y utilidades para *rate limiting*, *retries* y *logging*. -->

---

## 6) Indicadores y Visualizaciones

### 6.2 Gráficas (iniciales)
1. **Línea** Importaciones e importaciones
2. **Línea** Producto nacional bruto
3. **Línea** Variaciones trimestrales (QoQ)

---

## 7) Dashboard
- **Filtros:** Fecha inicial/final, transformación (QoQ).
- **Pestañas:**
  - **Explorar Series** (líneas con tooltips),
  - **Descargas** (PNG).

## 8) Librerías a utilizar:
- `requests`: para el API client
- `plotly express`: para visualización estadísticas (gráficas)
- `pandas`: para la manipulación de datos
- `dash`: mostrar un dashboard web

## 9) Presentación
- Se creo la presentación del proyecto en **quarto** la cual esta ubicada en la carpeta *presentacion_quarto*