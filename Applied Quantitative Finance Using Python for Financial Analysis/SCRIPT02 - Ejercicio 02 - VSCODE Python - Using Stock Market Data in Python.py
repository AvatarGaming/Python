# Importar las bibliotecas necesarias
# ffn: Para simplificar la recuperación de datos financieros desde Yahoo Finance.
# datetime: Para trabajar con fechas en Python.
# pandas_datareader: Complementario para trabajar con datos financieros, aunque no se usa directamente aquí.
import ffn
import datetime
import pandas_datareader as pdr

# Obtener datos históricos desde Yahoo Finance
# ffn.get(): Función que permite recuperar datos financieros de múltiples símbolos.
# 'aapl, spy, amzn': Símbolos de las acciones/ETF a recuperar (Apple, SPDR S&P 500, Amazon).
# start='2019-1-1': Fecha de inicio de los datos (1 de enero de 2019).
# end='2021-1-1': Fecha de fin de los datos (1 de enero de 2021).
stocks = ffn.get('aapl, spy, amzn', start='2019-1-1', end='2021-1-1')

# Mostrar las últimas filas del DataFrame
# stocks.tail(): Muestra las últimas 5 filas del conjunto de datos recuperado para una vista rápida.
print("Datos con precios ajustados por defecto:")
print(stocks.tail())

# Recuperar datos de precios de cierre regulares
# Cambiamos el acceso predeterminado al precio ajustado a precios de cierre regulares.
# 'aapl:Close, spy:Close, amzn:Close': Se especifica que deseamos los precios de cierre (Close) para cada acción.
stocks = ffn.get('aapl:Close, spy:Close, amzn:Close', start='2019-1-1', end='2021-1-1')

# Mostrar las últimas filas del DataFrame con precios de cierre regulares
print("\nDatos con precios de cierre regulares:")
print(stocks.tail())
