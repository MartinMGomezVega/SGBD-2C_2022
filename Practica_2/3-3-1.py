# Considerando solamente los deptos. de 3 ambientes, escribir un programa que grafique un boxplot de los precios de esos
# deptos. de las 5 ciudades mencionadas.
# Las 5 ciudades mencionadas son:
#   1. Buenos Aires
#   2. Cordoba
#   3. Rosario
#   4. La Plata
#   5. Mar del Plata

import pandas as pd
from pandas import Series, DataFrame
from matplotlib import pyplot as plt

# Leer el csv
dataframe = pd.read_csv('Practica_2\properati-AR-2018-02-01-properties-sell.csv')

# Duda con la ciudad Buenos Aires. 
# ¿tomamos capital federal o todas las localidades de Bs As?
dataFrameCiudades = dataframe[(((dataframe['state_name'] == ('Capital Federal'))) |
                        (dataframe['place_name'] == 'Córdoba') |
                        (dataframe['place_name'] == 'Rosario') |
                        (dataframe['place_name'] == 'La Plata') |
                        (dataframe['place_name'] == 'Mar del Plata')) &
                        (dataframe['property_type'] == 'apartment') & # deptos.
                        (dataframe['rooms'] == 3) & # ambientes
                        (dataframe['price_aprox_usd'] < 1000000)]

# Que el precio no sea nulo
dataFrameSinPrecioNulo = dataFrameCiudades[dataFrameCiudades.price_aprox_usd.notnull()]

# Mostrar Buenos Aires y no Capital Federal en el place_name (grafico)
# .loc se usa para acceder a un grupo de filas y columnas por etiqueta(s)
dataFrameSinPrecioNulo.loc[dataFrameSinPrecioNulo['state_name'] == 'Capital Federal', 'place_name' ] = 'Buenos Aires'

# Creacion del dataFrame que se va a utilizar para graficar con las columnas de referencia
dataFrameAGraficar = DataFrame(dataFrameSinPrecioNulo, columns=['place_name', 'price_aprox_usd'])

# Realizar el grafico boxplot con la columna price_aprox_usd y place_name ambas del dataFrameAGraficar 
dataFrameAGraficar.boxplot(column = ['price_aprox_usd'] , by = 'place_name')

plt.title("Precios de deptos. de 3 ambientes")
plt.xlabel("Ciudades")
plt.ylabel("Precios")
plt.show()

