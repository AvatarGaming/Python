# Importación de bibliotecas necesarias
# -------------------------------------
# NumPy: Realiza cálculos numéricos y operaciones matemáticas avanzadas.
import numpy as np  

# Pandas: Manipula y analiza datos estructurados en forma de DataFrames.
import pandas as pd  

# Matplotlib: Genera gráficos y visualizaciones 2D.
import matplotlib.pyplot as plt  

# datetime: Permite trabajar con fechas, como rangos de tiempo para análisis.
import datetime  

# yfinance: Biblioteca para descargar datos financieros de Yahoo Finance.
import yfinance as yf  

# Configuración para visualizar gráficos dentro de Jupyter Notebook
# Esto asegura que los gráficos se muestren directamente en el entorno.


# Definición de rango de fechas para el análisis
# ----------------------------------------------
# El análisis cubrirá datos desde el 1 de enero de 2015 hasta el 1 de enero de 2019.
start = datetime.datetime(2015, 1, 1)  # Fecha de inicio
end = datetime.datetime(2019, 1, 1)    # Fecha de fin


# Descarga de datos de Tesla desde Yahoo Finance
# ----------------------------------------------
# Se utiliza el ticker "TSLA" para obtener datos de Tesla, entre las fechas definidas.
# La función yf.download() descarga información como precios de apertura, cierre, volumen, etc.
tesla_data = yf.download('TSLA', start, end)


# Visualización básica de los datos descargados
# ---------------------------------------------
# Muestra las últimas 5 filas del DataFrame para observar los datos recientes.
print("Últimos 5 registros de datos descargados:")
print(tesla_data.tail())

# Muestra las primeras 5 filas del DataFrame para verificar los datos al inicio del rango.
print("\nPrimeros 5 registros de datos descargados:")
print(tesla_data.head())

