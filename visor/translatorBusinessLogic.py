from cgitb import reset
from unittest import result
from googletrans import Translator
from django.http import JsonResponse

def translate(targetSentence):
    translator = Translator()
    print("a traducir:", targetSentence)
    result =  translator.translate(targetSentence, src="es").text
    
    print("xxx: ", result)
    return  JsonResponse({"texto": result})