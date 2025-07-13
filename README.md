# 🎧 Analizador de Playlist de Spotify (desde CSV)

Este proyecto analiza una playlist exportada desde Spotify en formato CSV, generando estadísticas visuales, informes en texto y tablas detalladas. Ideal para amantes de la música que quieran descubrir más sobre sus hábitos de escucha.

---

## 🧰 Funcionalidades principales

### 📊 Estadísticas de artistas
- Top 10 artistas más frecuentes en tu playlist
- Gráfico de barras interactivo

### 📅 Análisis temporal
- Distribución por días de la semana
- Frecuencia por meses del año
- Gráficos de tendencia temporal

### 🔥 Descubrimiento musical
- Identificación de canciones menos populares
- Gráfico de dispersión de popularidad

### ⏱️ Análisis de duración
- Clasificación por cortas/medias/largas
- Gráfico circular de distribución

### 📝 Reporte completo
- Generación automática de informe en texto
- Formato tabular claro y legible

---

## 📂 Estructura del proyecto
```
analizador_playlist/
├── datos/                     # Datos de entrada
│   └── mi_playlist.csv        # Archivo CSV exportado desde Spotify
├── graficos/                  # Resultados visuales (autogenerado)
│   ├── artistas.png
│   ├── temporal.png
│   └── duracion.png
├── informes/                  # Reportes textuales
│   └── informe.txt
├── src/                       # Código fuente
│   ├── main.py                # Punto de entrada
│   ├── analisis.py            # Lógica de análisis
│   └── utils.py               # Funciones auxiliares
├── requirements.txt           # Dependencias
└── README.md                  # Documentación
```

---

## 🚀 Cómo usar

1. **Preparación del entorno:**

    ```bash
    python -m venv venv
    source venv/bin/activate     # Linux/Mac
    .\venv\Scripts\activate      # Windows
    pip install -r requirements.txt
    ```

2. **Preparar los datos:**  
   Exporta tu playlist desde Spotify usando [Exportify](https://exportify.net).  
   Coloca el archivo CSV en `datos/mi_playlist.csv`.

3. **Ejecuta el análisis:**

    ```bash
    python main.py
    ```

4. **Ver resultados:**  
   - Gráficos: en la carpeta `graficos/`  
   - Reporte completo: `informes/informe.txt`
