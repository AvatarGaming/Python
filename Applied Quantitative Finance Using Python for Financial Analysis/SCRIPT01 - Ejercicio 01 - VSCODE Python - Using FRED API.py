# =======================================================
# Script para Uso Básico de la API de FRED
# =======================================================
# Este script muestra un ejemplo sencillo de cómo usar la API de FRED para
# acceder a datos económicos como el Índice de Precios al Consumidor (CPI).

# =============================
# Importación de Bibliotecas
# =============================
# Bibliotecas estándar y de terceros necesarias para ejecutar el código
import datetime  # Para trabajar con fechas
from fredapi import Fred  # Biblioteca para interactuar con la API de FRED
import pandas as pd  # Para manejar y analizar datos en formato tabular

# =============================
# Configuración de la API de FRED
# =============================
# Ingresa tu clave API aquí (solicítala en: https://research.stlouisfed.org/docs/api/api_key.html)
fred = Fred(api_key='e6169f67af6efc86eb6c2289bff3111c')

# =============================
# Recuperación de Datos Históricos
# =============================
# Recuperamos el Índice de Precios al Consumidor (CPI) usando el código del indicador.
# "CPALTT01USM657N" es el código para el CPI de todos los artículos en EE. UU.
consumer_price_index = fred.get_series('CPALTT01USM657N')

# Mostramos las últimas 5 observaciones de los datos
print("\nÚltimos datos del Índice de Precios al Consumidor (CPI):")
print(consumer_price_index.tail())

# =============================
# Recuperación de Datos con Rango de Fechas
# =============================
# Establecemos un rango de fechas para filtrar los datos del CPI
start_date = datetime.datetime(2019, 1, 1)  # Fecha de inicio
end_date = datetime.datetime(2020, 9, 1)    # Fecha de fin

# Recuperamos los datos del CPI dentro del rango especificado
consumer_price_index_filtered = fred.get_series('CPALTT01USM657N', start_date, end_date)

# Mostramos las últimas 5 observaciones del rango filtrado
print("\nÚltimos datos del CPI para el rango de fechas especificado:")
print(consumer_price_index_filtered.tail())

# =============================
# Comentarios Finales
# =============================
# Este script proporciona un ejemplo básico de cómo interactuar con la API de FRED.
# Puedes modificar el código para trabajar con otros indicadores económicos