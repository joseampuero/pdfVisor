# visor/scripts/translatorScripts.py
import requests
from django.http import JsonResponse
from googletrans import Translator
from deep_translator import GoogleTranslator

def translate(targetSentence):
    """Función original para GET - mantiene compatibilidad"""
    return translate_with_direction(targetSentence, "en-es")

def translate_with_direction(targetSentence, direction="en-es"):    
    print(f"a traducir ({direction}): {targetSentence}")
    # 🌐 FALLBACK 0: Microservicio local (prioridad alta)
    try:
        response = requests.post(
            "http://localhost:43301/api/translate",
            json={"text": targetSentence, "direction": direction},
            timeout=10
        )
        if response.status_code == 200:
            result = response.json()["translation"]
            print(f"✅ traducido por microservicio local: {result}")
            return JsonResponse({"text": result})
        else:
            print(f"❌ Microservicio respondió con status: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("❌ Microservicio no disponible (¿está corriendo en puerto 43301?)")
    except requests.exceptions.Timeout:
        print("❌ Microservicio tardó más de 10 segundos")
    except Exception as e:
        print(f"❌ Error con microservicio local: {e}")
    
    # 🌐 FALLBACK 1: GoogleTranslator (online, buena calidad)
    try:
        if direction == "en-es":
            result = GoogleTranslator(source="en", target="es").translate(targetSentence)
        elif direction == "es-en":
            result = GoogleTranslator(source="es", target="en").translate(targetSentence)
        else:
            result = GoogleTranslator(source="auto", target="es").translate(targetSentence)
            
        print(f"✅ traducido por GoogleTranslator: {result}")
        return JsonResponse({"text": result})    
    except Exception as e:
        print(f"❌ Error con GoogleTranslator: {e}")

    # 🌐 FALLBACK 2: googletrans (online, última opción)
    try:     
        translator = Translator()
        if direction == "en-es":
            result = translator.translate(targetSentence, src="en", dest="es")
        elif direction == "es-en":
            result = translator.translate(targetSentence, src="es", dest="en")
        else:
            result = translator.translate(targetSentence, dest="es")
            
        text = result.text
        print(f"✅ traducido por googletrans: {text}")
        return JsonResponse({"text": text})    
    except Exception as e:
        print(f"❌ Error con googletrans: {e}")

    # 💥 Si todo falla
    print("💥 TODOS los traductores fallaron")
    return JsonResponse({
        "error": "Todos los traductores fallaron", 
        "text": targetSentence
    })