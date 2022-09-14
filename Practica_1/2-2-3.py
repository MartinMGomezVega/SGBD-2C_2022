# Realizar las siguientes visualizaciones:
# Un histograma de las 10 palabras representativas con mayor cantidad de ocurrencias en “king lear.txt” 
# (Ver seccion ”Bar Charts”, p´ag. 75 y 97)) https://www.geeksforgeeks.org/bar-plot-in-matplotlib/

# Una nube de palabras de las 50 palabras m´as representativas con mayor cantidad de ocurrencias en “king lear.txt”
# (Ver cap`ıtulo 20 del libro, p´ag. 334-336) https://www.datacamp.com/tutorial/wordcloud-python

# El objetivo de estas visualizaciones es intentar determinar algunas caracterısticas esenciales (ej.: el tema, los personajes,
# las acciones) del texto en base a la cantidad de ocurrencias de las palabras.
# Obs.: la noci´on de “palabra representativa” es subjetiva por lo tanto queda a criterio personal. Al menos habr´ıa que filtrar
# los adverbios, los art´ıculos y las proposiciones.

import procesamientoArchivo
import histograma
import nubePalabras

dictKingLear = procesamientoArchivo.volcarTextoEnDiccionario('Practica_1/king_lear.txt')
palabrasProhibidas = procesamientoArchivo.procesarTexto('Practica_1/palabras_prohibidas.txt')
procesamientoArchivo.eliminarPalabrasProhibidas(palabrasProhibidas, dictKingLear)

histograma.CrearHistogramaPalabrasCantidades(dictKingLear)
nubePalabras.CrearNubeDePalabras('Practica_1/king_lear.txt')
