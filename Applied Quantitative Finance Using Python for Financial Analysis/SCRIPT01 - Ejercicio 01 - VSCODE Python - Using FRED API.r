# =======================================================
# Script para Uso Básico de la API de FRED en R
# =======================================================
# Este script muestra un ejemplo sencillo de cómo usar la API de FRED para
# acceder a datos económicos como el Índice de Precios al Consumidor (CPI).

# =============================
# Importación de Bibliotecas
# =============================
library(fredr)  # Biblioteca para interactuar con la API de FRED
library(dplyr)  # Para manejar y analizar datos
library(lubridate)  # Para trabajar con fechas

# =============================
# Configuración de la API de FRED
# =============================
# Ingresa tu clave API aquí (solicítala en: https://research.stlouisfed.org/docs/api/api_key.html)
fredr_set_key("e6169f67af6efc86eb6c2289bff3111c")

# =============================
# Recuperación de Datos Históricos
# =============================
# Recuperamos el Índice de Precios al Consumidor (CPI) usando el código del indicador.
# "CPALTT01USM657N" es el código para el CPI de todos los artículos en EE. UU.
consumer_price_index <- fredr(series_id = "CPALTT01USM657N")

# Mostramos las últimas 5 observaciones de los datos
cat("\nÚltimos datos del Índice de Precios al Consumidor (CPI):\n")
print(tail(consumer_price_index))

# =============================
# Recuperación de Datos con Rango de Fechas
# =============================
# Establecemos un rango de fechas para filtrar los datos del CPI
start_date <- as.Date("2019-01-01")  # Fecha de inicio
end_date <- as.Date("2020-09-01")    # Fecha de fin

# Recuperamos los datos del CPI dentro del rango especificado
consumer_price_index_filtered <- fredr(
  series_id = "CPALTT01USM657N",
  observation_start = start_date,
  observation_end = end_date
)

# Mostramos las últimas 5 observaciones del rango filtrado
cat("\nÚltimos datos del CPI para el rango de fechas especificado:\n")
print(tail(consumer_price_index_filtered))

# =============================
# Comentarios Finales
# =============================
# Este script proporciona un ejemplo básico de cómo interactuar con la API de FRED.
# Puedes modificar el código para trabajar con otros indicadores económicos o realizar
# análisis más avanzados según tus necesidades.
