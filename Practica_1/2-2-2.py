#Escribir un programa basado en el punto anterior que considere filtrar el texto mediante un archivo de “palabras prohibidas”. Mas precisamente: se requiere crear un 
# archivo de texto que contenga una palabra por linea y aquellas palabras  “king lear.txt” que est´en contenidas en dicho archivo deben ser descartadas.
#El objetivo de este proceso de filtrado es descartar aquellas palabras que aportan poca informaci´on sobre un texto (ej.: adverbios, articulos, proposiciones).

import operator
import procesamientoArchivo

# - Ordenar de modo descendente las palabras por cantidad de ocurrencias
def sortDescDictionary(dict):
    return sorted(dict.items(), key=operator.itemgetter(1), reverse=True)
    

dictOrderDesc = sortDescDictionary(procesamientoArchivo.procesarTextoEnDiccionario('Practica_1/king_lear.txt'))

print("Cantidad de palabras que contiene el texto: " + str(len(dictOrderDesc)))

#  5 palabras mas usadas
i = 0
while i < 5:
    print (dictOrderDesc[i])
    i+=1  
