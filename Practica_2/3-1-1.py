#1. Calcular el valor medio de los deptos 2 ambientes en Capital Federal

import pandas


dataFrame = pandas.read_csv('Practica_2\properati-AR-2018-02-01-properties-sell.csv')
 
dfRequiredRows = dataFrame[(dataFrame['state_name'] == 'Capital Federal') 
              & (dataFrame['property_type'] == 'apartment') 
              & (dataFrame['rooms'] == 2) 
              & dataFrame['price_aprox_usd'].notnull()]

print(dfRequiredRows['price_aprox_usd'])

print("Valor medio de los deptos de 2 ambientes en Capital Federal: ")
print(dfRequiredRows['price_aprox_usd'].mean(skipna=True))