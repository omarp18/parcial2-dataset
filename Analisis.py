import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configuración para mostrar gráficos en VS Code
plt.switch_backend('TkAgg')  # O usa 'Qt5Agg' si tienes problemas

# 1. Verificar existencia del archivo
archivo_csv = 'temperatura_componentes.csv'
if not os.path.exists(archivo_csv):
    print(f"Error: No se encontró el archivo {archivo_csv}")
    print("Por favor ejecuta primero el script de generación de datos")
    exit()

# 2. Cargar los datos
try:
    df = pd.read_csv(archivo_csv)
    print("Dataset cargado exitosamente!")
    print(f"Total de registros: {len(df)}")
except Exception as e:
    print(f"Error al cargar el dataset: {e}")
    exit()

# 3. Análisis básico
print("\n=== ESTADÍSTICAS BÁSICAS ===")
print(df.describe())

# 4. Estadísticas por componente
print("\n=== ESTADÍSTICAS POR COMPONENTE ===")
stats_componentes = df.groupby('component_id').agg({
    'temperatura': ['mean', 'median', 'std', 'max'],
    'is_anomalo': 'sum'
})
print(stats_componentes)

# 5. Análisis de anomalías
print("\n=== ANÁLISIS DE ANOMALÍAS ===")
anomalias = df[df['is_anomalo']]
print(f"Total anomalías: {len(anomalias)} ({len(anomalias)/len(df)*100:.2f}%)")
print("\nTipos de anomalía:")
print(anomalias['tipo_anomalia'].value_counts())

# 6. Visualizaciones
print("\nGenerando visualizaciones...")

# Gráfico 1: Distribución de temperaturas
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='temperatura', bins=30, kde=True)
plt.title('Distribución de Temperaturas')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Frecuencia')
plt.show()

# Gráfico 2: Temperaturas por componente
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='component_id', y='temperatura')
plt.title('Distribución de Temperaturas por Componente')
plt.xlabel('Componente')
plt.ylabel('Temperatura (°C)')
plt.xticks(rotation=45)
plt.show()

# Gráfico 3: Matriz de correlación
numeric_cols = ['temperatura', 'normal_temp_min', 'normal_temp_max']
plt.figure(figsize=(8, 6))
sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm', center=0)
plt.title('Matriz de Correlación')
plt.show()

print("\n¡Análisis completado con éxito!")