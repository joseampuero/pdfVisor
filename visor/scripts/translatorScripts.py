from googletrans import Translator
from django.http import JsonResponse
from deep_translator import GoogleTranslator

def translate(targetSentence):    
    print("a traducir:", targetSentence)
    
    try:
        result = GoogleTranslator(source="en", target="es").translate(targetSentence)
        print("traducido por googleTrans: ", result)
        return  JsonResponse({"text": result})    
    except:
        print("Ha ocurrido un error con GoogleTranlator")

    try:     
        translator = Translator()
        result =  translator.translate(targetSentence, src="en", dest="es")
        text = result.text

        print("traducido por translator: ", text)
        return  JsonResponse({"text": text})    
    except:
        print("Ha ocurrido un error con Translator")

    return