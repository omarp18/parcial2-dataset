import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Configuración para la generación de datos
np.random.seed(42)
num_registros = 1000
componentes = ['CPU', 'GPU', 'RAM', 'SSD', 'Motherboard']

# Generar timestamps (últimos 7 días, cada ~10 minutos)
timestamps = [datetime.now() - timedelta(days=7) + timedelta(minutes=10*i) for i in range(num_registros)]

# Generar datos
data = {
    'timestamp': timestamps,
    'component_id': np.random.choice(componentes, num_registros),
    'temperatura': np.concatenate([
        np.random.normal(40, 5, 900),  # Datos normales
        np.random.normal(80, 10, 50),   # Picos de temperatura
        np.random.normal(70, 5, 50)    # Sobrecalentamiento sostenido
    ]),
    'normal_temp_min': np.random.choice([30, 35, 40, 25, 45], num_registros),
    'normal_temp_max': np.random.choice([60, 65, 70, 55, 75], num_registros)
}

# Crear DataFrame
df = pd.DataFrame(data)

# Asegurar que temp_min < temp_max
df['normal_temp_min'] = np.minimum(df['normal_temp_min'], df['normal_temp_max'] - 5)
df['normal_temp_max'] = np.maximum(df['normal_temp_max'], df['normal_temp_min'] + 5)

# Determinar anomalías
df['is_anomalo'] = (df['temperatura'] < df['normal_temp_min']) | (df['temperatura'] > df['normal_temp_max'])
df['tipo_anomalia'] = '-'
df.loc[(df['is_anomalo']) & (df['temperatura'] > df['normal_temp_max'] + 15), 'tipo_anomalia'] = 'spike'
df.loc[(df['is_anomalo']) & (df['temperatura'] > df['normal_temp_max'] + 5) & (df['temperatura'] <= df['normal_temp_max'] + 15), 'tipo_anomalia'] = 'sustained_overheat'

# Guardar dataset
df.to_csv('temperatura_componentes.csv', index=False)

print("Dataset generado exitosamente!")
print(f"Total de registros: {len(df)}")
print(f"Anomalías detectadas: {df['is_anomalo'].sum()}")