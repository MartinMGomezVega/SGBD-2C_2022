# Enunciado:
# Dado un string con el siguiente formato: “nombre1,apellido1,DNI1/.../nombreN,apellidoN,DNIN”, escribir un programa
# que lo procese y escriba la siguiente información por pantalla:
# apellido1 nombre1
# . . .
# apellidoN nombreN

import re

def procesarString():
    stringExample = "martin,gomez,41702705,miguel,vega,50720714"
    splitedStr = stringExample.split(",")
    
    for word in splitedStr:
        match = re.search('([a-zA-Z]+)', word)
        if (bool(match)):
            print(word)
       

procesarString()