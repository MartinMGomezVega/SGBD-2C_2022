#Trini
#Escribir un programa basado en el punto anterior que considere filtrar el texto mediante un archivo de “palabras prohibidas”. Mas precisamente: se requiere crear un 
# archivo de texto que contenga una palabra por linea y aquellas palabras  “king lear.txt” que est´en contenidas en dicho archivo deben ser descartadas.
#El objetivo de este proceso de filtrado es descartar aquellas palabras que aportan poca informaci´on sobre un texto (ej.: adverbios, articulos, proposiciones).

from hashlib import new
import re

# Archivo:
archivoKingLear = open('Practica_1/king_lear.txt')
archivoPalabrasProhibidas = open('Practica_1/palabras_prohibidas.txt')

# - Pasar las palabras a minúsculas
archivoEnMinusculas = (archivo.read()).lower()
#print (archivoEnMinusculas)

# - Descartar los signos de puntuación (sobre el archivoEnMinusculas)
archSinSignosPuntuacion = re.sub(r'[^\w\s]','',archivoEnMinusculas)
# print(archSinSignosPuntuacion)

# - Separar y contar las ocurrencias de las palabras (Evaluar si conviene utilizar un “dict” o la clase “collections.Counter” de python)
listaPalabras = archSinSignosPuntuacion.split()

def listaPalabrasDicFrec(listaPalabras):
    frecuenciaPalab = [listaPalabras.count(p) for p in listaPalabras]
    return dict(list(zip(listaPalabras,frecuenciaPalab)))

dictArch = listaPalabrasDicFrec(listaPalabras)
#print (dictArch)

# - Ordenar de modo descendente las palabras por cantidad de ocurrencias
def sortDescDictionary(dictArch):
    aux = [(dictArch[key], key) for key in dictArch]
    aux.sort()
    aux.reverse() #Descendente
    return aux

dictOrderDesc = sortDescDictionary(dictArch)
#print(dictOrderDesc)

# Responder
#   • ¿Cuántas palabras tiene el texto?
cantidadPalabras = len(re.findall(r'\w+', archivoEnMinusculas))
#print("Cantidad de palabras que contiene el texto: " + str(cantidadPalabras))

#   • ¿Cuáles son las 5 palabras más usadas?
i = 0
while i < 5:
    print (dictOrderDesc[i])
    i+=1  
