# Proyecto de Predicción de Ventas

## 📊 Descripción
Este proyecto implementa un modelo de predicción de ventas utilizando regresión lineal para pronosticar las ventas de los primeros tres meses del año 2025, basándose en los datos históricos de ventas del año 2024.

## 🚀 Características
- Análisis de series temporales de datos de ventas
- Implementación de modelo de regresión lineal
- Visualización gráfica de datos históricos y predicciones
- Generación de pronósticos para los primeros tres meses de 2025
- Exportación de resultados en formato visual

## 📋 Requisitos
- Python 3.8+
- Bibliotecas de Python:
  - pandas
  - numpy
  - scikit-learn
  - matplotlib

## 🛠️ Instalación
1. Clona este repositorio:
   ```bash
   git clone https://github.com/conecta-media/prediccion-de-ventas.git
   cd prediccion-de-ventas
   ```

2. Crea y activa un entorno virtual (recomendado):
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # o
   source .venv/bin/activate  # Linux/Mac
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
   
   Si no existe el archivo requirements.txt, instala las dependencias manualmente:
   ```bash
   pip install pandas numpy scikit-learn matplotlib openpyxl
   ```

## 🚀 Uso
1. Asegúrate de tener un archivo Excel con los datos de ventas históricas en el mismo directorio.
2. Ejecuta el script principal:
   ```bash
   python prediccion_ventas.py
   ```
3. El script generará:
   - Gráfico de ventas históricas vs predicciones
   - Resultados de las predicciones en la consola

## 📊 Estructura del Proyecto
```
.
├── .venv/                  # Entorno virtual (ignorado por git)
├── prediccion_ventas.py    # Script principal de predicción
├── Ventas.xlsx            # Datos de ventas (ejemplo)
├── Ventas Excel real.xlsx  # Datos reales de ventas
├── Predicción de ventas enero.png  # Gráfico generado
└── README.md              # Este archivo
```

## 📈 Resultados
El modelo genera predicciones para los primeros tres meses de 2025 basadas en los datos históricos de 2024. Los resultados incluyen:
- Gráfico comparativo de ventas reales vs. predicciones
- Valores numéricos de las predicciones en la consola

## 📝 Notas Adicionales
- Los datos de ejemplo están incluidos en el repositorio.
- Asegúrate de que los archivos de datos estén en el mismo directorio que el script.
- El modelo utiliza regresión lineal simple, lo que puede no ser adecuado para patrones de ventas complejos.

## 🤝 Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue primero para discutir los cambios que te gustaría realizar.