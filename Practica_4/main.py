import pymongo


MONGO_HOST="localhost"
MONGO_PORT="27017"
MONGO_TIEMPO_FUERA=1000
MONGO_URI="mongodb://"+MONGO_HOST+":"+MONGO_PORT+"/"
MONGO_BASEDATOS = "test"
MONGO_COLECCION_TWEETS = "tweets"

try:
    db=pymongo.MongoClient(MONGO_URI,serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)
    bd=db[MONGO_BASEDATOS]
    colTweets=bd[MONGO_COLECCION_TWEETS]

    db.server_info()
    print("Conexion a MongoDB exitosa")

except:
    print("Error en la conexion a la base")
    

    
    
    
def p31():
#1. Seleccionar el id y el texto de 10 “documents”
    print("PUNTO 1")
    resultado = colTweets.find({}, {"text":1}).limit(10);
    for i in resultado:
        print(i)
        
#2. Seleccionar los lenguajes distintos de los tweets
    print("PUNTO 2")
    resultado = colTweets.distinct( "lang" )
    for i in resultado:
        print(i)

#3. Seleccionar el id, el nombre, la descripcion y la cantidad de followers de aquellos usuarios que tengan mas de 100000 followers
    print("PUNTO 3")
    resultado = colTweets.find({"user": {"$elemMatch": {"followers_count": {"$gt": 30 }}}})
    for i in resultado:
        print(i)
    
    resultado = colTweets.find({"user.followers_count": {"$gt": 100000 }},{"_id":1, "user.name":1, "user.description":1, "user.followers_count":1})
    for i in resultado:
        print(i)

#4. Seleccionar el id, el nombre y la cantidad de followers de los 10 usuarios con mas followers ordenado de manera descendente


#Seleccionar el id, el nombre y la cantidad de followers de los 10 usuarios con m´as followers ordenado de manera descendente
    print("PUNTO 4")

def p33():
    #Listar los 10 usuarios que publicaron m´as tweets (ordenarlos de manera descendente por cantidad de tweets
    resultado = colTweets.aggregate(
    [
        {
            "$group": {"_id": {"Usuario":"$user.name"}, "Cantidad" : {"$sum":1}} },
        {
            "$sort":{"Cantidad":-1}},{"$limit":10} 
    
     ]                   )

#Listar por lenguaje la cantidad de followers del usuario con mayor cantidad de followers que publica en ese lenguaje
    resultado_2 = colTweets.aggregate(
    [ 
     {
         "$group" : { "_id" : "$user.lang", "max" :{"$max" : "$user.followers_count"}}}
     ,{
         "$sort" : { "max":-1}}]) 


    print("resultado 3.3.1")
    for i in resultado:
        print(i)
    
    print("resultado 3.3.2")
    for i in resultado_2:
        print(i)
    
#31()
#p33()


re =  colTweets.find({},{"_id":0,"user.id" : 1,"user.followers_count": 1,"user.name":1}).sort([("user.followers_count",pymongo.DESCENDING)]).limit(10)

for i in re:
    print(i)