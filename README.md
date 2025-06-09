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
   python generar_dataset.py
2. **Analizar los datos**:
   ```bash
   python analizar_dataset.py
Requisitos
Python 3.6+

Bibliotecas requeridas (instalar con pip install -r requirements.txt):
   ```bash
pandas
numpy
matplotlib
seaborn
![Figure_1](https://github.com/user-attachments/assets/90ec8f94-fd56-407e-8e56-41b0758ffe79)

![Figure_2](https://github.com/user-attachments/assets/92907741-8c74-43cd-8bb7-8468452491f0)

![Figure_3](https://github.com/user-attachments/assets/a0d39ce9-d1d8-4c3a-ac9a-fe62c60efe44)
