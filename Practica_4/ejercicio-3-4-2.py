import matplotlib.pyplot as plt
from geopandas import GeoDataFrame
import pymongo as mongo

#Mapa vacio
mapa = GeoDataFrame.from_file('ne_10m_admin_0_countries.shp')

#Conexion con mongo
MONGO_HOST="localhost"
MONGO_PUERTO="27017"
MONGO_URI="mongodb://"+MONGO_HOST+":"+MONGO_PUERTO+"/"
conexionMongo = mongo.MongoClient(MONGO_URI)
MONGO_BASEDATOS = conexionMongo["test"]
MONGO_COLECCION = MONGO_BASEDATOS["tweets"]

#Guardar los datos en el mapa
i = 0
for location in MONGO_COLECCION.aggregate([{"$group":{"_id":{"codigo":"$codigo","pais":"$pais"},"population":{"$sum":1}}},{ "$sort": {"population": -1}}]):
	codigoWorld = location.get('_id').get('codigo')
	paisWorld = location.get('_id').get('pais')
	populationWorld = location.get('population')

	mapa.loc[mapa['NAME'] == paisWorld, 'population'] = populationWorld
	mapa.loc[mapa['SOV_A3'] == codigoWorld, 'population'] = populationWorld
	mapa.loc[mapa['SOV_A3'] == codigoWorld, 'escala'] = i
	mapa.loc[mapa['NAME'] == paisWorld, 'escala'] = i
	i = i + 1

mapa.plot(column='escala', colormap='Reds', alpha=1, categorical=False, legend=False, axes=None)
plt.show()