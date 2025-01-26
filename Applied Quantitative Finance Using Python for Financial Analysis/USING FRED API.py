# """
# uso_de_la_api_de_fred.py
# USO DE LA API DE FRED PARA INDICADORES ECONÓMICOS
# Este script muestra cómo instalar, configurar y utilizar la API de FRED para recuperar datos económicos,
# como el Índice de Precios al Consumidor (CPI) de los Estados Unidos.

# Secciones:
# 1. Instalación de la API de FRED
# 2. Configuración de la API de FRED
# 3. Recuperación de datos históricos del CPI
# 4. Recuperación de datos específicos con un rango de fechas
# """



import datetime  # Importamos las bibliotecas estándar primero
from fredapi import Fred  # Luego las bibliotecas de terceros
import pandas as pd

# ==========================================
# SECCIÓN 1: Instalación de la API de FRED
# ==========================================
# Antes de ejecutar este script, instala la biblioteca ejecutando el siguiente comando en la terminal o en Jupyter Notebook:
# !pip install fredapi
# ==========================================

# ==========================================
# SECCIÓN 2: Configuración de la API de FRED
# ==========================================
# Ingresa tu clave API aquí (solicítala en: https://research.stlouisfed.org/docs/api/api_key.html)
fred = Fred(api_key='e6169f67af6efc86eb6c2289bff3111c')

# ==========================================
# SECCIÓN 3: Recuperación de datos históricos del CPI
# ==========================================
# Recuperamos el Índice de Precios al Consumidor: Todos los Artículos (CPALTT01USM657N)
# para los Estados Unidos y mostramos las últimas 5 observaciones.
consumer_price_index = fred.get_series('CPALTT01USM657N')  # Código del indicador
print("Últimos datos del Índice de Precios al Consumidor (CPI):")
print(consumer_price_index.tail())  # Muestra las últimas 5 observaciones

# ==========================================
# SECCIÓN 4: Recuperación de datos con rango de fechas
# ==========================================
# Establecemos el rango de fechas
start_date = datetime.datetime(2019, 1, 1)  # Fecha de inicio
end_date = datetime.datetime(2020, 9, 1)    # Fecha de fin

# Recuperamos los datos del CPI dentro del rango de fechas especificado
consumer_price_index_filtered = fred.get_series('CPALTT01USM657N', start_date, end_date)

# Mostramos las últimas 5 observaciones de los datos filtrados
print("\nÚltimos datos del CPI para el rango de fechas especificado:")
print(consumer_price_index_filtered.tail())
