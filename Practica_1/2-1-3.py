#Escribir un programa que elimine los signos de puntuaci´on de un string.

import re

string = '!hola. c?omo, esta- el cli[m]a ho?y.'
reGex = r'[^\w\s]'

print(re.sub(reGex, '', string))