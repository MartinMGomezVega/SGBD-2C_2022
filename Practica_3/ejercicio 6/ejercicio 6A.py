# En base al ejemplo “prueba.py”, realizar siguientes gr´aficos Choropleth (https://en.wikipedia.org/wiki/Choropleth_map):
#    1. Un mapa de la poblaci´on mundial

import matplotlib.pyplot as plt
import psycopg2
from geopandas import GeoDataFrame

mapa = GeoDataFrame.from_file('ne_10m_admin_0_countries.shp')

try:
  conexionBD = psycopg2.connect(database = 'mapa', user = 'postgres', host = 'localhost', password = '1327')
  cursor = conexionBD.cursor()
  query = "SELECT name,code,population FROM country ORDER BY population;"
  cursor.execute(query)
  resultados = cursor.fetchall() #resultados en forma de lista
  
  i = 0
  for row in resultados:		
    mapa.loc[mapa['NAME'] == row[0], 'population'] = row[2]
    mapa.loc[mapa['SOV_A3'] == row[1], 'population'] = row[2]
    mapa.loc[mapa['SOV_A3'] == row[1], 'escala'] = i
    mapa.loc[mapa['NAME'] == row[0], 'escala'] = i
    i = i + 1

except (Exception, psycopg2.Error) as error:
  print ("No se pudieron cargar los datos", error)
finally:
  if (conexionBD): #se cierra la conexion a la base
    cursor.close()
    conexionBD.close()

mapa.plot(column='escala', colormap='Reds', alpha=1, categorical=False, legend=False, axes=None)
plt.show()

