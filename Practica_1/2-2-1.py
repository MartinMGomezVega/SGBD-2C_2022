# Enunciado:
# Escribir un programa para procesar el archivo “king lear.txt”:
# - Pasar las palabras a minúsculas
# - Descartar los signos de puntuación
# - Separar y contar las ocurrencias de las palabras (Evaluar si conviene utilizar un “dict” o la clase “collections.Counter” de python)
# - Ordenar de modo descendente las palabras por cantidad de ocurrencias
# Responder
#   • ¿Cuántas palabras tiene el texto?
#   • ¿Cuáles son las 5 palabras más usadas?

import operator
import re

# Archivo:
archivo = open('Practica_1/king_lear.txt')

# - Pasar las palabras a minúsculas
archivoEnMinusculas = (archivo.read()).lower()

# - Descartar los signos de puntuación (sobre el archivoEnMinusculas)
archSinSignosPuntuacion = re.sub(r'[^\w\s]','',archivoEnMinusculas)

# - Separar y contar las ocurrencias de las palabras (Evaluar si conviene utilizar un “dict” o la clase “collections.Counter” de python)
listaPalabras = archSinSignosPuntuacion.split()

def guardarPalabrasEnDict():
    wordDict = dict()
    for palabra in listaPalabras:
        if (palabra in wordDict):
            wordDict[palabra] =  wordDict.get(palabra) + 1
        else:
            wordDict[palabra] = 1
    return wordDict

# - Ordenar de modo descendente las palabras por cantidad de ocurrencias
def sortDescDictionary():
    return sorted(guardarPalabrasEnDict().items(), key=operator.itemgetter(1), reverse=True)
    

dictOrderDesc = sortDescDictionary()

# Responder
#   • ¿Cuántas palabras tiene el texto?
cantidadPalabras = len(re.findall(r'\w+', archivoEnMinusculas))
print("Cantidad de palabras que contiene el texto: " + str(cantidadPalabras))

#   • ¿Cuáles son las 5 palabras más usadas?
i = 0
while i < 5:
    print (dictOrderDesc[i])
    i+=1  
