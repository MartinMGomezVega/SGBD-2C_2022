#Escribir un programa que reconozca los s´ımbolos de los n´umeros romanos: recibe un string S por teclado e imprime
#“TRUE” si todos los caracteres de S corresponden a s´ımbolos de n´umeros romanos o “FALSE” en caso contrario. Por
#ejemplo:
#input: “XL” → output: “TRUE”
#input “#CienciaDeDatos” → output: “FALSE”
import re


def numerosRomanos():
    string = "XL,II,#CienciaDeDatos,hola,40955681,XXI,V"
    reGex = '^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
    strArray = string.split(",")
    
    for word in strArray:
      match =  bool(re.search(reGex, word))
      print ("#input: " + word + " -> output: " + str(match))
        
numerosRomanos() 