# Realizar las siguientes visualizaciones:
# Un histograma de las 10 palabras representativas con mayor cantidad de ocurrencias en “king lear.txt” 
# (Ver seccion ”Bar Charts”, p´ag. 75 y 97))
# Una nube de palabras de las 50 palabras m´as representativas con mayor cantidad de ocurrencias en “king lear.txt”
# (Ver cap`ıtulo 20 del libro, p´ag. 334-336)
# El objetivo de estas visualizaciones es intentar determinar algunas caracterısticas esenciales (ej.: el tema, los personajes,
# las acciones) del texto en base a la cantidad de ocurrencias de las palabras.
# Obs.: la noci´on de “palabra representativa” es subjetiva por lo tanto queda a criterio personal. Al menos habr´ıa que filtrar
# los adverbios, los art´ıculos y las proposiciones.

import re
import matplotlib.pyplot as plot
import pandas as pd
import seaborn as sb

with open('Practica_1/king_lear.txt', 'r') as f:
    texto = f.read()

textoSinSignos = re.sub(r'[^\w\s]','',texto)

# Lista de palabras convertidas en minuscula
palabras = textoSinSignos.lower().split()

def ContadorPalabrasRepetidas(p, palabras):
    """ Cuenta las palabras de la lista """
    return {p:palabras.count(p)}

# Lista de diccionarios con key: palabra y value: n. de veces repetida
dict_list = [ContadorPalabrasRepetidas(p, palabras) for p in palabras]
# Elimina los resultados repetidos 
resultados = [i for n, i in enumerate(dict_list) if i not in dict_list[n + 1:]] 
# Ordena los resultados
res_ordenados = sorted(resultados, key=lambda d: list(d.values()), reverse=True)
# Obtiene los primeros 10 resultados
diezPalabrasRecurrentes = res_ordenados[:10]

def ObtenerDiezPalabrasMasUsadas():
    listaPalabras = []
    for d in diezPalabrasRecurrentes:
        for key, value in d.items():
            #print(key, value, sep=': ')
            listaPalabras.append(key)
    return listaPalabras
    
listaX = ObtenerDiezPalabrasMasUsadas()
print(listaX)

def ObtenerDiezValoresMasUsadas():
    listaValores = []
    for d in diezPalabrasRecurrentes:
        for key, value in d.items():
            #print(key, value, sep=': ')
            listaValores.append(value)
    return listaValores

listaY = ObtenerDiezValoresMasUsadas()
print(listaY)

edades = [12, 15, 13, 12, 18, 20, 19, 20, 13, 12, 13, 17, 15, 16, 13, 14, 13, 17, 19]

intervalos = range(min(edades), max(edades) + 2)

sb.displot(edades, color='#F2AB6D', bins=intervalos, kde=True) #creamos el gráfico en Seaborn

#configuramos en Matplotlib
plot.xticks(rangos)
plot.ylabel('Frecuencia')
plot.xlabel('Edades')
plot.title('Histograma de las 10 palabras mas usadas en “king lear.txt” ')
plot.show()

# Un histograma de las 10 palabras representativas con mayor cantidad de ocurrencias en “king lear.txt” (Ver sección 'Bar Charts', pág. 75 y 97))
# Una nube de palabras de las 50 palabras más representativas con mayor cantidad de ocurrencias en “king lear.txt” (Ver capítulo 20 del libro, pág. 334-336)
# El objetivo de estas visualizaciones es intentar determinar algunas características esenciales (ej.: el tema, los personajes,
# las acciones) del texto en base a la cantidad de ocurrencias de las palabras.

