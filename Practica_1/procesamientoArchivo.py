import re

def procesarTextoEnDiccionario(nombreArchivo):
  archivo = open(nombreArchivo)
  archivoEnMinusculas = (archivo.read()).lower()
  archSinSignosPuntuacion = re.sub(r'[^\w\s]','',archivoEnMinusculas)
  dict = guardarPalabrasEnDict(archSinSignosPuntuacion.split())
  return dict

def guardarPalabrasEnDict(listaPalabras):
    wordDict = dict()
    for palabra in listaPalabras:
        if (palabra in wordDict):
            wordDict[palabra] =  wordDict.get(palabra) + 1
        else:
            wordDict[palabra] = 1
    return wordDict
