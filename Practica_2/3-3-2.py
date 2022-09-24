# Basandose en el gr´afico anterior, responder a las siguientes preguntas:
#   1. ¿Cual es la ciudad con mayor costo de vida? Justificar
#   2. ¿Cual es la ciudad mas equitativa? Justificar
#   3. Proponer algunos argumentos por los cuales podrıa ser incorrecto deducir las dos respuestas anteriores del conjunto de datos que estamos utilizando

import pandas as pd
from pandas import Series, DataFrame
from matplotlib import pyplot as plt
import numpy as np
import funciones

# Leer el csv
df = pd.read_csv('Practica_2\properati-AR-2018-02-01-properties-sell.csv')

dataframe = df[(((df['state_name'] == ('Capital Federal'))) |
                        (df['place_name'] == 'Córdoba') |
                        (df['place_name'] == 'Rosario') |
                        (df['place_name'] == 'La Plata') |
                        (df['place_name'] == 'Mar del Plata')) &
                        (df['property_type'] == 'apartment') & # deptos.
                        (df['rooms'] == 3) & # ambientes
                        (df['price_aprox_usd'] > 0)]



# 1. ¿Cual es la ciudad con mayor costo de vida?
funciones.ciudadConMayorCostoDeVida(dataframe)

# 2. ¿Cual es la ciudad mas equitativa?
funciones.ciudadMasEquitativa(dataframe)
