

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


MONGO_HOST="localhost"
MONGO_PORT="27017"
MONGO_TIEMPO_FUERA=1000
MONGO_URI="mongodb://"+MONGO_HOST+":"+MONGO_PORT+"/"
MONGO_BASEDATOS = "test"
MONGO_COLECCION_TWEETS = "tweets"

hostname = 'localhost'
database ='postgresDB'
username = 'admin'
pwd = 'admin'
portId = '5455'

def actualziarMongo():
    try:
        cliente=pymongo.MongoClient(MONGO_URI,serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)
        baseDatos=cliente[MONGO_BASEDATOS]
        coleccion_tw=baseDatos[MONGO_COLECCION_TWEETS]
        baseDatos=cliente[MONGO_BASEDATOS]
        collection = baseDatos[MONGO_COLECCION_TWEETS]
        
        cliente.server_info()
        print("BD Mongo OK!")
    except:
        print("BD Mongo : FAIL!")
        
    cursor = collection.find({})

    
    for i in cursor:
        _id = i['id']
        userLocation = i['user']['location']
        print("ID: ",i['user']['id'])
        print("-> ",userLocation)
        value = "No information"
        if (userLocation != None):
            value = obtenerCodigoPais(userLocation)
        query = {"id": _id}
        print(value)
        newValues = {"$set": {'countryCode': value}}
        collection.update_one(query, newValues)

def obtenerCodigoPais(userLocation):
    diccionarioCitiesNameCountry = devolverDiccionario(
        'SELECT name, countrycode FROM city')
    diccionarioCitiesDistrictCountry = devolverDiccionario(
        'SELECT district, countrycode FROM city')
    diccionarioCountries = devolverDiccionario(
        'SELECT name, code FROM country')
    value = 'X'

    for i in diccionarioCountries.keys():
            if (userLocation in i or i in userLocation):
                value = diccionarioCountries[i]
                break
            
    if (value == 'X'):
        for i in diccionarioCitiesNameCountry.keys():
            if (userLocation in i or i in userLocation):
                value = diccionarioCitiesNameCountry[i]
                break
    
    if (value == 'X'):
        for i in diccionarioCitiesDistrictCountry.keys():
            if (userLocation in i or i in userLocation):
                value = diccionarioCitiesDistrictCountry[i]
                break
    
    if (value == 'X'):
        print("Nada disponible")

    return value

def conectarBD():
    try:
        conexion = psycopg2.connect(
            user = username, 
            password = pwd, 
            host = hostname, 
            port = portId, 
            database = "postgresDB")

    except (Exception, psycopg2.Error) as error:
        print ("BD postgres : FAIL!", error)
        
    return conexion


def crearDiccionario(query):
    conexion = conectarBD()
    cur = conexion.cursor()
    cur.execute(query)
    fila = cur.fetchone()
    diccionario = {}
    
    while fila is not None:
            clave = fila[0]
            valor = fila[1] 
            diccionario[clave] = valor
            fila = cur.fetchone()

    cur.close()
    cerrarConexion(conexion)

    return diccionario

def devolverDiccionario(query):
    diccionario = crearDiccionario(query)
    return diccionario

def cerrarConexion(conexion):
    if(conexion):
        conexion.close()
    else:
        print("Close conection FAIL!")
        

def graficarMapaTweets():
    try:
    
        cliente=pymongo.MongoClient(MONGO_URI,serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)
        baseDatos=cliente[MONGO_BASEDATOS]
        coleccion_tw=baseDatos[MONGO_COLECCION_TWEETS]
        baseDatos = cliente.test
        collection = baseDatos['tweets']
        print("BD Mongo OK!")
    except:
        print("BD Mongo : FAIL!")
    cursor = collection.find({})
    values = []
    dicPaises = devolverDiccionario(
        'SELECT name, code FROM country')
    diccionario = {}
    for idx, i in enumerate(cursor):    
        if("countryCode" in i.keys() and idx < 50000):
            values.append(i['countryCode'])

    for i in dicPaises.keys():
        diccionario[dicPaises[i]] = values.count(dicPaises[i])

    print("Progresando....")
    dataFrame = pd.DataFrame(list(diccionario.items()), columns=['codigoPais', 'cantidad'])
 
    fig = px.choropleth(dataFrame, locations='codigoPais', color='cantidad', scope="world")
    fig.show()
        
        
def main():
    actualziarMongo()
    #graficarMapaTweets()

    
main()