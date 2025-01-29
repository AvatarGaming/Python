# Importación de bibliotecas necesarias
import pandas as pd
import datetime
from fredapi import Fred  # Asegúrate de tener la librería 'fredapi' instalada

# Configuración de la clave de la API de FRED
fred = Fred(api_key='e6169f67af6efc86eb6c2289bff3111c')

# Sección 1: Definición del rango de fechas
# Definir las fechas de inicio y fin para los datos a analizar
start = datetime.datetime(2015, 1, 1)
end = datetime.datetime(2020, 12, 31)

# Sección 2: Descarga de datos desde FRED
# Descargar datos del PIB para Brasil, China y Estados Unidos utilizando los códigos FRED correspondientes
br_data = fred.get_series("BRAGDPNQDSMEI", start, end)
ch_data = fred.get_series("CHNGDPNQDSMEI", start, end)
us_data = fred.get_series("USAGDPNQDSMEI", start, end)

# Combinar los datos en un solo DataFrame
# Unir las series de datos en un DataFrame con las columnas correspondientes a cada país
gdp_comparison = pd.concat([br_data, ch_data, us_data], axis=1, join="inner")
gdp_comparison.columns = ["Brasil", "China", "Estados Unidos"]

# Mostrar las últimas filas del DataFrame
print("Datos combinados:\n", gdp_comparison.tail())

# Sección 3: Renombrar las columnas
# Cambiar los nombres de las columnas a inglés para estandarizar
print("Renombrando las columnas...")
gdp_comparison = gdp_comparison.rename(columns={"Brasil": "Brazil", "China": "China", "Estados Unidos": "USA"})
print("Columnas renombradas:\n", gdp_comparison.head())

# Sección 4: Cálculo del cambio porcentual
# Calcular el cambio porcentual para analizar el crecimiento relativo del PIB entre trimestres
gdp_change = gdp_comparison.pct_change() * 100
print("Cambio porcentual (primeras filas):\n", gdp_change.head())

# Sección 5: Limpieza de datos
# Eliminar filas con valores nulos (NA) para preparar los datos para graficar o análisis adicional
gdp_change = gdp_change.dropna()
print("Cambio porcentual después de eliminar NA:\n", gdp_change.head())

# Sección 6: Conclusión
# El DataFrame resultante contiene los cambios porcentuales del PIB para cada país, listo para análisis o visualización.
