# Determinar el origen de los usuarios basandose en: el campo “user.location” y la base de datos “world” de la pr´actica 3.
# Agregar un campo nuevo en cada “document” que explicite el pa´ıs de origen del usuario. Una idea ser´ıa hacer chequeos
# incrementales que se ejecuten secuencialmente, por ejemplo:
# Si el campo “user.location” contiene un nombre de pa´ıs, considero ese como pa´ıs del usuario
# Los usuarios de EEUU muchas veces escriben su ubicaci´on de forma “Ciudad,Estado” (ej.: “Washington, DC”).
# En ese caso hay que matchear el estado y si es v´alido hay que colocar “us” como pa´ıs
# etc.

import pymongo

def conectMongoDB():
    MONGO_HOST="localhost"
    MONGO_PUERTO="27017"
    MONGO_TIEMPO_FUERA=1000

    MONGO_URI="mongodb://"+MONGO_HOST+":"+MONGO_PUERTO+"/"

    MONGO_BASEDATOS="test"
    MONGO_COLECCION="tweets"

    try:
        cliente=pymongo.MongoClient(MONGO_URI,serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)
        baseDatos=cliente[MONGO_BASEDATOS]
        coleccion=baseDatos[MONGO_COLECCION]
        for documento in coleccion.find("user.").limit(3):
            print(documento["id"])
        #cliente.server_info()
        #print("Coneccion a mongo exitosa")
        cliente.close()
    except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
        print("Tiempo exedido "+errorTiempo)
    except pymongo.errors.ConnectionFailure as errorConexion:
        print("Fallo al conectarse a mongodb "+errorConexion)


conectMongoDB()

# Agregar un nuevo campo en la coleccion:
# db.vehiculos.update({},{$set:{"activo":"si"}},{upsert:false,multi:true})
# db.tweets.find({},{_id:1, "user.location":1}).limit(10);
