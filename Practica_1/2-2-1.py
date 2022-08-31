# Enunciado:
# Escribir un programa para procesar el archivo “king lear.txt”:
# - Pasar las palabras a minúsculas
# - Descartar los signos de puntuación
# - Separar y contar las ocurrencias de las palabras (Evaluar si conviene utilizar un “dict” o la clase “collections.Counter” de python)
# - Ordenar de modo descendente las palabras por cantidad de ocurrencias
# Responder
#   • ¿Cuántas palabras tiene el texto?
#   • ¿Cuáles son las 5 palabras más usadas?

import procesamientoArchivo 

dictKingLear = procesamientoArchivo.volcarTextoEnDiccionario('Practica_1/king_lear.txt')
procesamientoArchivo.palabrasConMayorAparicion(dictKingLear)
