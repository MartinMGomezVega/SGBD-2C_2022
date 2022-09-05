import re
import operator
import procesamientoArchivo
import numpy as np
import matplotlib.pyplot as plt

def CrearHistogramaPalabrasCantidades(diccionarioLibro):
    result = procesamientoArchivo.ObtenerPalabrasConMayorOcurrencia(diccionarioLibro) # 10
    palabras = list(result.keys())
    cantidad = list(result.values())
    fig = plt.figure(figsize = (10, 5))
    plt.bar(palabras, cantidad, color ='blue', width = 0.4)
    plt.title("Histograma")
    plt.xlabel("Palabras")
    plt.ylabel("Cantidad de ocurrencias")
    plt.show()

