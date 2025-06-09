# Análisis de Temperatura de Componentes de Computadora

Este proyecto genera y analiza un dataset simulado de temperaturas de componentes de computadora, detectando posibles anomalías térmicas.

## Estructura del Proyecto
/proyecto-temperaturas
│ Creacion.py
│ Analisis.py
│ temperatura_componentes.csv
│ README.md

## Dataset Generado

El dataset contiene las siguientes columnas:

- `timestamp`: Fecha y hora de la medición
- `component_id`: Identificador del componente (CPU, GPU, RAM, etc.)
- `temperatura`: Temperatura medida en °C
- `normal_temp_min`: Temperatura mínima normal para el componente
- `normal_temp_max`: Temperatura máxima normal para el componente
- `is_anomalo`: Indicador booleano de anomalía (True/False)
- `tipo_anomalia`: Tipo de anomalía detectada ('spike', 'sustained_overheat' o '-')

## Cómo Usar

1. **Generar el dataset**:
   ```bash
   python Creacion.py
2. **Analizar los datos**:
   ```bash
   python Analisis.py
Requisitos
Python 3.6+

Bibliotecas requeridas (instalar con pip install -r requirements.txt):
   ```bash
pandas
numpy
matplotlib
seaborn
