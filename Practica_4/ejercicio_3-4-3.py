#  Basado en el punto 1, elegir 2 paıses y realizar una nube de palabras (una para cada paıs) de las 20 palabras mas
# usadas en los campos “text” de los tweets de esos dos 2 paıses

#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
import collections
from matplotlib import pyplot as plt
import pymongo as mongo
from wordcloud import WordCloud, STOPWORDS

#Conexion con la base de datos de mongo
myClient = mongo.MongoClient("mongodb://localhost:27017/")
myTest = myClient["test"]
myTweets = myTest["tweets"]

archivoProhibido = open('Practica_4/nube.txt','r')
strProhibido = archivoProhibido.read()
archivoProhibido.close()
#Descartar palabras prohibidas
palabrasProhibidas = re.split(r'\W+',strProhibido)

def convert(string):
    li = re.split(r'\W+',string)
    return li


def obtenerTexto (pais):
    cnt = collections.Counter()
    for location in myTweets.find({"pais": pais},{"text": 1, "_id":0}):
        texto = location.get('text')
        #Pasar las palabras a minuscula
        tweet = texto.lower()
        if (":" in tweet):
            tweet = tweet.split(":", 1)[1]
        
        #Descartar los signos de puntuacion
        tweet = re.sub(r'[^a-z0-9\s]','',tweet)
        
        for palabraProhibida in palabrasProhibidas:
            tweet = re.sub('\s' + palabraProhibida + '\s',' ', tweet)
        
        #Separar y contar las ocurrencias de las palabras
        for word in convert(tweet):
            cnt[word] += 1
            
    data = cnt.most_common(20)
    return data


def text_size(total):
    return total

#Genera la nube de palabras que va a ser graficada
def generarNube(pais):
    data = obtenerTexto(pais)
    wordcloud = WordCloud(
            background_color='white',
            stopwords=STOPWORDS,
            max_words=20,
            max_font_size=40, 
            scale=4,
            random_state=1
        ).generate(str(data))
    
    return wordcloud
    
#Grafica las dos nubes de palabras
def graficarNube(): 
    paises = ["Argentina", "Brazil"]

    y = 1
    for pais in paises:
        wordcloud = generarNube(pais)
        
        fig = plt.figure(1, figsize=(12, 12))
        fig.add_subplot(1,2,y)
        plt.imshow(wordcloud)
        plt.title(pais)
        plt.axis('off')
        y += 1

    plt.show()


graficarNube()