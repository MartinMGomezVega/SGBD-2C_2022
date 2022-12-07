# En base al punto anterior, realizar un Mapa Choropleth que refleje por cada paıs la cantidad total de tweets vinculados
# a usuarios de ese paıs

import matplotlib.pyplot as plt
from geopandas import GeoDataFrame
import pymongo as mongo

#Mapa vacio
mapa = GeoDataFrame.from_file('Practica_4/ne_10m_admin_0_countries.shp')

#Conexion con mongo
MONGO_HOST="localhost"
MONGO_PUERTO="27017"
MONGO_URI="mongodb://"+MONGO_HOST+":"+MONGO_PUERTO+"/"
conexionMongo = mongo.MongoClient(MONGO_URI)
MONGO_BASEDATOS = conexionMongo["test"]
MONGO_COLECCION = MONGO_BASEDATOS["tweets"]


# ARREGLARLO!


#Guardar los datos en el mapa
i = 0
for location in MONGO_COLECCION.aggregate([{"$group":{"_id":{"codigo":"$codigo","pais":"$pais"},"tweets":{"$sum":1}}},{ "$sort": {"tweets": -1}}]):
	codigoWorld = location.get('_id').get('codigo')
	paisWorld = location.get('_id').get('pais')
	tweetsWorld = location.get('tweets')

	mapa.loc[mapa['NAME'] == paisWorld, 'tweets'] = tweetsWorld
	mapa.loc[mapa['SOV_A3'] == codigoWorld, 'tweets'] = tweetsWorld
	mapa.loc[mapa['SOV_A3'] == codigoWorld, 'escala'] = i
	mapa.loc[mapa['NAME'] == paisWorld, 'escala'] = i
	i = i + 1

mapa.plot(cmap='Reds', alpha=1, categorical=False, legend=False, ax=None)
plt.show()