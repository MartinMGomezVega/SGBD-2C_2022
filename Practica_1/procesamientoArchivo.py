import re
import operator

def volcarTextoEnDiccionario(nombreArchivo):
  dict = guardarPalabrasEnDict(procesarTexto(nombreArchivo))
  return dict


def guardarPalabrasEnDict(listaPalabras):
    wordDict = dict()
    for palabra in listaPalabras:
        if (palabra in wordDict):
            wordDict[palabra] =  wordDict.get(palabra) + 1
        else:
            wordDict[palabra] = 1
    return wordDict


def procesarTexto(nombreArchivo):
  archivo = open(nombreArchivo)
  archivoEnMinusculas = (archivo.read()).lower()
  return re.sub(r'[^\w\s]','',archivoEnMinusculas).split()


def palabrasConMayorAparicion(diccionario):
  dictOrderDesc = sorted(diccionario.items(), key=operator.itemgetter(1), reverse=True)
  print("Cantidad de palabras que contiene el texto: " + str(len(dictOrderDesc)))
  for i in range(0,5):
    print (dictOrderDesc[i])
    

def ObtenerPalabrasConMayorOcurrencia(diccionario):
  dictResult = {}
  dictOrderDesc = sorted(diccionario.items(), key=operator.itemgetter(1), reverse=True)
  i = 0
  for (key, value) in dictOrderDesc:
    if(i < 10):
      i += 1
      dictResult[key] = value
        
    
  return dictResult
