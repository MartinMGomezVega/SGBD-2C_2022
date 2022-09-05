import re
import operator
import procesamientoArchivo
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from wordcloud import STOPWORDS, WordCloud

def CrearNubeDePalabras(texto):
    text = open(texto, mode="r", encoding="utf-8").read()
    stopwords = STOPWORDS

    wc = WordCloud(background_color="white", stopwords=stopwords, height=600, width=400)
    wc.generate(text)

    # store to file
    wc.to_file("Practica_1/wordcloud_output.png")
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show() 
    
