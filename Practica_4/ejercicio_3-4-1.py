
 #for location in collectionTweets.find({}, {"user.location": 1, "codigo": 1, "pais": 1, "_id": 0}):
          #  print(location)
import pymongo
import psycopg2
import psycopg2.extras
from csv import reader
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import rcParams
from pandas import DataFrame, Series, read_csv
from pymongo import MongoClient
from seaborn.palettes import dark_palette
import plotly.express as px
import random
import psycopg2


MONGO_HOST = "localhost"
MONGO_PORT = "27017"
MONGO_TIEMPO_FUERA = 1000
MONGO_URI = "mongodb://"+MONGO_HOST+":"+MONGO_PORT+"/"
MONGO_BASEDATOS = "test"
MONGO_COLECCION_TWEETS = "tweets"

hostname = 'localhost'
database = 'postgresDB'
username = 'admin'
pwd = 'admin'
portId = '5455'


def actualziarMongo():
    try:

        cliente = pymongo.MongoClient(
            MONGO_URI, serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)
        baseDatos = cliente[MONGO_BASEDATOS]
        collectionTweets = baseDatos[MONGO_COLECCION_TWEETS]

        cliente.server_info()

        print("BD Mongo OK!")

    except:
        print("BD Mongo : FAIL!")

    # Creacion del campo codigo
    collectionTweets.update_many({}, {"$set": {"user.codigo": "null"}})
    collectionTweets.update_many({}, {"$set": {"user.pais": "null"}})

    try:
        conexionPostgres = psycopg2.connect(
            user=username,
            password=pwd,
            host=hostname,
            port=portId,
            database="postgresDB")
        
        print("BD Postgres OK!")

    except (Exception, psycopg2.Error) as error:
        print("BD postgres : FAIL!", error)

    cursor = conexionPostgres.cursor()

    countryQuery = 'SELECT name, code, localname FROM country order by name;'
    cursor.execute(countryQuery)
    countryData = cursor.fetchall()

    cityQuery = "select city.name, city.countrycode, country.name from city inner join country on city.countrycode = country.code;"
    cursor.execute(cityQuery)
    cityData = cursor.fetchall()

    tweetsCol = collectionTweets.find(
        {}, {"user.location": 1, "codigo": 1, "_id": 0})

    for location in tweetsCol:

        codigo = ""
        pais = ""
        state = False

        localizacion = location.get("user").get("location")

        
        if(localizacion != None):
            if ('THE UNITED STATES OF AMERICA' in localizacion or 'NY' in localizacion or 'U.S.A' in localizacion or 'Arizona' in localizacion or 'TX' in localizacion or 'Florida' in localizacion or 'Texas' in localizacion):
                state = True
                codigo = 'USA'
                pais = 'United States'
                
            elif ('CABA' in localizacion or 'Buenos Aire' in localizacion or 'BS.AS' in localizacion):
                state = True
                codigo = 'ARG'
                pais = 'Argentina'
                
            elif (state == False):
                
                for row in countryData:
                    if (row[0] in localizacion and state == False):
                        state = True
                        codigo = row[1]
                        pais = row[0]
                        break
                    
                    elif (row[1] in localizacion and state == False):
                        state = True
                        codigo = row[1]
                        pais = row[0]
                        break
                    
                    elif (row[2] in localizacion and state == False):
                        state = True
                        codigo = row[1]
                        pais = row[0]
                        break

                if (state == False):
                    for fila in cityData:
                        if (fila[0] in localizacion):
                            state = True
                            codigo = fila[1]
                            pais = fila[2]
                            
        nuevoValores = {"$set": 
            {
                "user.codigo": codigo, 
                "user.pais": pais
            }
        }
        updates = collectionTweets.update_many(
            {
                "user.location": localizacion
            }
            , nuevoValores)
        
        
        print("*******-user location: ",localizacion)
        print("__pais: ",pais)
        print("__codigo: ",codigo)
        
        #print(updates)
       


def main():
    actualziarMongo()
    # graficarMapaTweets()


main()
