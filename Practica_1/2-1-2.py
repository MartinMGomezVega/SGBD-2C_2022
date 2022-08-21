# Enunciado:
# Dado un string con el siguiente formato: “nombre1,apellido1,DNI1/.../nombreN,apellidoN,DNIN”, escribir un programa
# que lo procese y escriba la siguiente información por pantalla:
# apellido1 nombre1
# . . .
# apellidoN nombreN

import re


def functionStringFormat():
    str = "martin,gomez,41702705,miguel,vega,50720714"
    matches = re.finditer('([a-zA-Z]+.),([a-zA-Z]+)+', str) # Coincide con un patrón en una cadena y devuelve un iterador que produce los Matchobjetos de todas las coincidencias que no se superponen.
    
    # Recorrer matches y mostrar el valor
    for matchNum, match in enumerate(matches, start=1):
        print (("{match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group(2)))+
               " "+
               "{match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group(1)))
        
functionStringFormat() 