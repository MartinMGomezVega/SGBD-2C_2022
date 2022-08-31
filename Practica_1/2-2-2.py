#Escribir un programa basado en el punto anterior que considere filtrar el texto mediante un archivo de “palabras prohibidas”. 
# Mas precisamente: se requiere crear un archivo de texto que contenga una palabra por linea y 
# aquellas palabras  “king lear.txt” que estén contenidas en dicho archivo deben ser descartadas.
#El objetivo de este proceso de filtrado es descartar aquellas palabras que aportan poca información sobre un texto (ej.: adverbios, articulos, proposiciones).

import procesamientoArchivo  

dictKingLear = procesamientoArchivo.volcarTextoEnDiccionario('Practica_1/king_lear.txt')
palabrasProhibidas = procesamientoArchivo.procesarTexto('Practica_1/palabras_prohibidas.txt')

def eliminarPalabrasProhibidas():
    for palProhib in palabrasProhibidas:
        if (palProhib in dictKingLear):
            dictKingLear.pop(palProhib)


eliminarPalabrasProhibidas()
procesamientoArchivo.palabrasConMayorAparicion(dictKingLear)
