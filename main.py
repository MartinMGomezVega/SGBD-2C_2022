from googletrans import Translator
translator = Translator()
textoSalida = translator.translate('Hola Mundo', dest='en')
print(textoSalida.text)