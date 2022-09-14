#PPara aquellas propiedades de Capital Federal que tengan informacion geograﬁca se pide escribir un programa para hacer un scatterplot de las propiedades que 
# diﬁeran a lo sumo en 0.05 grados en latitud y longitud respecto al centro 
# geograﬁco de la ciudad. Obs.: obtener las coordenadas del centro de la ciudad de modo aproximado con googlemaps).


from pandas import DataFrame
import pandas
from matplotlib import pyplot as plt

LATITUD_CENTRO = -34.617008
LONGITUD_CENTRO = -58.445095

dataFrame = pandas.read_csv('Practica_2\properati-AR-2018-02-01-properties-sell.csv')

dfRequiredRows = dataFrame[(dataFrame['state_name'] == 'Capital Federal')]
dfRequiredRows = dfRequiredRows[dfRequiredRows.lat.notnull() & dfRequiredRows.lon.notnull()]

dfFiltered = DataFrame(dfRequiredRows, columns=['lat', 'lon'])
dfFiltered = dfFiltered[(dfFiltered['lat'] <= LATITUD_CENTRO + 0.05) & (dfFiltered['lat'] >= LATITUD_CENTRO - 0.05)]
dfFiltered = dfFiltered[(dfFiltered['lon'] <= LONGITUD_CENTRO + 0.05) & (dfFiltered['lon'] >= LONGITUD_CENTRO - 0.05)]

dfFiltered.plot.scatter(x='lon', y='lat')

plt.xlabel("Longitud")
plt.ylabel("Latitud")
plt.title("PROPIEDADES CAPITAL FEDERAL")
plt.show()