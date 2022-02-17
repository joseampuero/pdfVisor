from googletrans import Translator
from django.http import JsonResponse

def translate(targetSentence):
    translator = Translator()
    print("a traducir:", targetSentence)
    result =  translator.translate(targetSentence, src="en", dest="es")
    text = result.text
    print("oracion tradicida: ", text)
    return  JsonResponse({"text": text})