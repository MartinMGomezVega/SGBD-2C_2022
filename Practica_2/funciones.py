import pandas as pd
from pandas import Series, DataFrame
from matplotlib import pyplot as plt
import numpy as np

def ciudadConMayorCostoDeVida(dataframe):
    df = dataframe[dataframe.price_aprox_usd.notnull()]
    # Indice de precio aprox usd maximo
    indiceMax = df['price_aprox_usd'].idxmax()
    # place_name del id con maximo price_aprox_usd
    placeMax = df['place_name'][indiceMax]
    # state_name del id con maximo price_aprox_usd
    stateMax = df['state_name'][indiceMax]
    # Mayor costo de vida
    costo = df['price_aprox_usd'][indiceMax]
    # Si el state es Capital Federal, el place_name pasa a ser Buenos Aires ya que se encuentra en esta ciudad
    if(stateMax == 'Capital Federal'):
        df.loc[df['state_name'] == 'Capital Federal', 'place_name' ] = 'Buenos Aires'
        placeMax = df['place_name'][indiceMax]
        print ("La ciudad con mayor costo de vida es : " + str(placeMax) +" - "+ str(stateMax) + " | Costo: " + str(costo))
    else:
        print ("La ciudad con mayor costo de vida es : " + str(placeMax) +" - "+ str(stateMax) + " | Costo: " + str(costo))
        
def ciudadMasEquitativa(dataframe):
    df = dataframe[dataframe.price_aprox_usd.notnull()]
    # ordenar el dataframe de mayor a menor (descendente)
    dfOrderDesc = df.sort_values(by =['price_aprox_usd'], ascending=False)
    # cantidad de lineas
    cantValores = dfOrderDesc.shape[0]
    # Obtener el valor de la mitad de la cantidad de lineas totales
    valorMedio = int(cantValores / 2)
    print("La ciudad mas equitativa es: "+ str(dfOrderDesc.iloc[valorMedio]['place_name']) +
          " - "+ str(dfOrderDesc.iloc[valorMedio]['state_name']) +
          " | Costo: "+ str(dfOrderDesc.iloc[valorMedio]['price_aprox_usd']))