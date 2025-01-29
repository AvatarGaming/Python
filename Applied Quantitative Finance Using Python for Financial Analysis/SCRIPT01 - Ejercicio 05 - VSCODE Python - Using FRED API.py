# Importar librerías necesarias
from fredapi import Fred
import datetime

# Inicializar la API de FRED con la clave de acceso
fred = Fred(api_key='e6169f67af6efc86eb6c2289bff3111c')

# ===========================
# Obtener el PIB nominal (2017)
# ===========================
# Definir el rango de fechas para el año base 2017
start_2017 = datetime.datetime(2017, 1, 1)
end_2017 = datetime.datetime(2017, 12, 31)

# Obtener la serie temporal del PIB nominal ("GDP")
nominal_GDP = fred.get_series('GDP', start_2017, end_2017)
print("PIB Nominal (2017):\n", nominal_GDP.tail())  # Mostrar las últimas entradas

# ===========================
# Obtener el PIB real (2019)
# ===========================
# Definir el rango de fechas para el año de comparación 2019
start_2019 = datetime.datetime(2019, 1, 1)
end_2019 = datetime.datetime(2019, 12, 31)

# Obtener la serie temporal del PIB real ("GDPC1")
real_GDP = fred.get_series('GDPC1', start_2019, end_2019)
print("PIB Real (2019):\n", real_GDP)  # Mostrar los datos obtenidos

# ===========================
# Calcular la suma de PIB nominal y real
# ===========================
# Sumar los valores del PIB nominal para el año base
ngdp_sum = nominal_GDP.sum()
ngdp_sum = int(ngdp_sum)  # Convertir a entero
print("Suma del PIB Nominal (2017):", ngdp_sum)

# Sumar los valores del PIB real para el año de comparación
rgdp_sum = real_GDP.sum()
rgdp_sum = int(rgdp_sum)  # Convertir a entero
print("Suma del PIB Real (2019):", rgdp_sum)

# ===========================
# Calcular el Deflactor del PIB
# ===========================
# Utilizar la fórmula del Deflactor del PIB
# GDPDeflator = (nominalGDP / realGDP) × 100
deflator = (ngdp_sum / rgdp_sum) * 100

# Mostrar el resultado del deflactor
print("Deflactor del PIB:", deflator)

# Verificar el tipo de dato del resultado
print("Tipo de dato del Deflactor:", type(deflator))
