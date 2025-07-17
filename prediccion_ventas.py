# Paso 1: Importar librerías
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Paso 2: Crear los datos históricos de ventas
ventas = {
    'Mes': ['2024-01', '2024-02', '2024-03', '2024-04', '2024-05', '2024-06',
            '2024-07', '2024-08', '2024-09', '2024-10', '2024-11', '2024-12'],
    'Ventas': [49.5, 52.0, 59.2, 53.7, 48.7, 52.0, 54.2, 53.5, 48.5, 47.2, 53.5, 52.2]
}

# Crear el DataFrame
df = pd.DataFrame(ventas)

# Verificar datos cargados
print("Datos cargados:")
print(df.head())

# Convertir la columna 'Mes' a formato datetime y establecer como índice
df['Mes'] = pd.to_datetime(df['Mes'])
df.set_index('Mes', inplace=True)

# Renombrar la columna de ventas si es necesario (opcional, ya se llama 'Ventas')
# df.rename(columns={'Ventas promedio': 'Ventas'}, inplace=True)  # No necesario en este caso

# Paso 3: Preparar los datos para la regresión lineal
x = np.arange(len(df)).reshape(-1, 1)  # Números enteros como variable independiente (meses)
y = df['Ventas'].values  # Ventas como variable dependiente

# Paso 4: Entrenar el modelo de regresión lineal
model_rl = LinearRegression()
model_rl.fit(x, y)

# Paso 5: Predecir Enero - Marzo 2025
x_pred = np.array([len(df), len(df)+1, len(df)+2]).reshape(-1, 1)
predicciones = model_rl.predict(x_pred)

# Paso 6: Crear DataFrame con las predicciones
fechas_pred = pd.date_range(start='2025-01-01', periods=3, freq='MS')
df_pred = pd.DataFrame({'Mes': fechas_pred, 'Ventas': np.round(predicciones, 2)})
df_pred.set_index('Mes', inplace=True)

# Unir datos reales y predicciones
df_completo = pd.concat([df, df_pred])

# Graficar resultados
plt.figure(figsize=(12, 6))

# Gráfico de ventas reales
plt.plot(df.index, df['Ventas'], label='Ventas Reales 2024', color='blue', marker='o')
for i in df.index:
    plt.text(i, df.loc[i, 'Ventas'] + 0.5, str(round(df.loc[i, 'Ventas'])), ha='center', fontsize=9, color='blue')

# Gráfico de predicciones
plt.plot(df_pred.index, df_pred['Ventas'], label='Predicciones (2025)', color='red', marker='x', linestyle='--')
for i in df_pred.index:
    plt.text(i, df_pred.loc[i, 'Ventas'] + 0.5, str(round(df_pred.loc[i, 'Ventas'])), ha='center', fontsize=9, color='red')

# Estética del gráfico
plt.title("Predicción de Ventas Enero - Marzo 2025 (Regresión Lineal)")
plt.xlabel("Mes")
plt.ylabel("Ventas Promedio")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Imprimir predicciones en consola
print("\nPredicciones Regresión Lineal:")
for fecha, valor in zip(df_pred.index.strftime('%b %Y'), df_pred['Ventas']):
    print(f"{fecha}: {valor:.2f} ventas")