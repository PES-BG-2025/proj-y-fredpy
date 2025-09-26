# Propuesta de Proyecto (Python)  
## “Indicadores Externos y Actividad Económica con FRED: Exportaciones, Importaciones y PIB”

## 1) Resumen
Construiremos un **pipeline de datos en Python** para consultar la API de **FRED** (Federal Reserve Bank of St. Louis), obtener **series temporales de Exportaciones, Importaciones y PIB** de EE. UU., y producir:
1) **Gráficas comparables** (niveles y tasas de variación),
2) **Indicadores derivados** (Balanza comercial y participación de comercio exterior vs PIB),
3) Un **dashboard interactivo** (Streamlit o Dash) para explorar periodos, frecuencias y transformaciones.

El resultado permitirá analizar la relación entre el sector externo y la actividad económica de forma reproducible y extensible.

---

## 2) Objetivos
- **O1.** Consumir la API de FRED de forma programática y robusta (módulo Python reusable).
- **O2.** Estandarizar y documentar el **proceso ETL** (extracción, transformación y carga).
- **O3.** Generar **visualizaciones** y un **dashboard** con filtros por rango de fechas, frecuencia y transformación (nivel, % interanual, variación trimestral).
- **O4.(Opcional; si el tiempo lo permite)** Publicar **artefactos reproducibles**: código, `requirements.txt`, README y notas técnicas.

---

## 3) Alcance y Entregables
### 3.1 Datos meta (iniciales)
- **PIB** (real y/o nominal, trimestral).
- **Exportaciones de Bienes y Servicios** (trimestral).
- **Importaciones de Bienes y Servicios** (trimestral).

**Nota:** Las IDs exactas de FRED se parametrizarán. Evitamos hardcodear IDs para facilitar mantenimiento.

<!-- ### 3.2 Entregables ()
- **Repositorio Git** con:
  - `fred_client.py` (módulo de consultas a FRED),
  - `etl.py` (limpieza/transformaciones),
  - `viz.py` (gráficas base),
  - `app.py` (dashboard Streamlit/Dash),
  - `tests/` (pruebas unitarias básicas),
  - `config.sample.toml` (API key y parámetros),
  - `requirements.txt` y `README.md`.
- **Dashboard** con:
  - Selector de series, rango de fechas y transformación,
  - 3 vistas clave: *Niveles*, *Crecimientos*, *Comercio/PIB*,
  - Exportación de gráficos/CSV.
- **Informe breve** (PDF/Markdown) con metodología y hallazgos. 
-->

---

## 4) Metodología y Arquitectura

- **Autenticación:** API Key de FRED `config.toml`.
- **Frecuencias:** Trimestral (base)
- **Transformaciones:** 
  - Nivel,
  - **Δ% interanual (YoY)**,
  - **Δ% trimestral (QoQ)**,
  - **Índice base = 100** en fecha seleccionada.
- **Manejo de calidad:**
  - Validación de fechas y frecuencia consistente,
  - Tests de forma (no vacíos, columnas esperadas).

---

## 5) Endpoints de FRED a utilizar (plan)
- **Búsqueda de series:** `GET /fred/series/search`  
  - Uso: encontrar IDs para “GDP”, “Exports of Goods and Services”, “Imports of Goods and Services”.
- **Datos de series:** `GET /fred/series/observations`  
  <!-- - Parámetros: `series_id`, `observation_start`, `observation_end`, `frequency`, `aggregation_method`, `output_type`. -->
  Parámetros: `series_id`, `observation_start`, `observation_end`, `output_type`.
- **Metadatos de series (opcional):** `GET /fred/series`
<!-- 
> Se implementarán **funciones wrapper**:  
> `search_series(query, limit=5)`, `get_series(series_id, params)`, y utilidades para *rate limiting*, *retries* y *logging*. -->

---

## 6) Indicadores y Visualizaciones

### 6.1 Indicadores
- **Balanza Comercial (BC):** \( \text{BC}_t = \text{Export}_t - \text{Import}_t \)
- **Apertura Comercial (% del PIB):** \( \frac{\text{Export}_t + \text{Import}_t}{\text{PIB}_t} \times 100 \)
- **Crecimientos:** YoY y QoQ para cada serie.

### 6.2 Gráficas (iniciales)
1. **Líneas: Exportaciones vs Importaciones** (niveles y BC en panel alterno o toggle).
2. **Barras/Línea combinada:** Balanza Comercial en barras con línea de media móvil.
3. **Líneas:** PIB y (Export+Import)/PIB (%).

---

## 7) Dashboard
- **Filtros:** Fecha inicial/final, transformación (Nivel/YoY/QoQ/Índice), selección de series.
- **Pestañas:**
  - **Explorar Series** (líneas con tooltips),
  - **Balanza y Apertura** (métricas derivadas),
  - **Descargas** (CSV/PNG).

## 8) Librerías a utilizar:
- **request:** para el API client
- **plotly express:** para visualización estadísticas (gráficas)
- **pandas:** para la manipulación de datos
- **dash**: mostrar un dashboard web
