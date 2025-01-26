# Importación de bibliotecas necesarias
from fredapi import Fred  # API para acceder a datos económicos de la Reserva Federal
import datetime  # Manejo de fechas

# Configuración del período de tiempo
start = datetime.datetime(2019, 1, 1)  # Fecha inicial: 1 de enero 2019
end = datetime.datetime(2020, 9, 1)    # Fecha final: 1 de septiembre 2020

# Inicialización de la conexión a FRED
# Nota: Es recomendable mantener la API key en una variable de entorno por seguridad
fred = Fred(api_key='e6169f67af6efc86eb6c2289bff3111c')

# Obtención del PIB real (GDPC1)
# GDPC1: PIB real ajustado estacionalmente en billones de dólares de 2012
gdp = fred.get_series('GDPC1', start, end)
print(gdp.tail())  # Muestra los últimos 5 registros del PIB

# Cálculo de la variación porcentual del PIB
gdp_change = gdp.pct_change() * 100  # Multiplicamos por 100 para obtener porcentaje
print(gdp_change.tail())  # Muestra los últimos 5 registros de la variación