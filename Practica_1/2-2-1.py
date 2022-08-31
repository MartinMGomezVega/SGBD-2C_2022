# Enunciado:
# Escribir un programa para procesar el archivo “king lear.txt”:
# - Pasar las palabras a minúsculas
# - Descartar los signos de puntuación
# - Separar y contar las ocurrencias de las palabras (Evaluar si conviene utilizar un “dict” o la clase “collections.Counter” de python)
# - Ordenar de modo descendente las palabras por cantidad de ocurrencias
# Responder
#   • ¿Cuántas palabras tiene el texto?
#   • ¿Cuáles son las 5 palabras m´as usadas?

from hashlib import new
import re

# Archivo:
archivo = open('Practica_1/king_lear.txt')

# - Pasar las palabras a minúsculas
archivoEnMinusculas = (archivo.read()).lower()
#print (archivoEnMinusculas)

# - Descartar los signos de puntuación (sobre el archivoEnMinusculas)
archSinSignosPuntuacion = re.sub(r'[^\w\s]','',archivoEnMinusculas)
# print(archSinSignosPuntuacion)

# - Separar y contar las ocurrencias de las palabras (Evaluar si conviene utilizar un “dict” o la clase “collections.Counter” de python)
listaPalabras = archSinSignosPuntuacion.split()

# Implementarlo de distinta forma. (RESOLVER)
def listaPalabrasDicFrec(listaPalabras):
    frecuenciaPalab = [listaPalabras.count(p) for p in listaPalabras]
    return dict(list(zip(listaPalabras,frecuenciaPalab)))

dictArch = listaPalabrasDicFrec(listaPalabras)
#print (dictArch)

# - Ordenar de modo descendente las palabras por cantidad de ocurrencias
def sortDescDictionary(dictArch):
    # sorted() ver como resolver con el sorted
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
# ¿Contar las palabras distintas!

#   • ¿Cuáles son las 5 palabras más usadas?

def cincoPalabrasMasUsadas():    
    i = 0
    while i < 10:
        print (dictOrderDesc[i])
        diezPalabras = dictOrderDesc[i]
        i+=1  

cincoPalabrasMasUsadas()