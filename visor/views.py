from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from visor.scripts import translatorScripts, visorScripts, storageScripts, learnScript
from visor.serializers import textSerializer
from visor.models import Text
import constants
import json

def visor(request, file, fromPage, toPage):
    pdfPath = visorScripts.findFilePath(file, constants.ROOT_PATH)
    print("el path es ", pdfPath)

    text = visorScripts.loadOnDemand(pdfPath, fromPage, toPage)
    textToLoad = Text(text, fromPage, toPage)
    textSerialized = textSerializer.TextSerializer(textToLoad)
    
    storageScripts.manageTempData(textSerialized.data)

    return JsonResponse(textSerialized.data)

def translator(request, sentence):
    """GET - Para palabras individuales y frases cortas"""
    return translatorScripts.translate(sentence)

@csrf_exempt  # Para permitir POST desde frontend
def translator_post(request):
    """POST - Para frases largas y caracteres especiales"""
    if request.method == 'POST':
        try:
            # Leer el JSON del body
            data = json.loads(request.body)
            sentence = data.get('sentence', '')
            direction = data.get('direction', 'en-es')  # Opcional: dirección
            
            if not sentence.strip():
                return JsonResponse({'error': 'Sentence is required'}, status=400)
            
            # Usar la misma función de traducción
            return translatorScripts.translate_with_direction(sentence, direction)
            
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)

def learn(request, fromPage, toPage):
    learnScript.learningHandler(fromPage, toPage)
    return JsonResponse({"status": "success"})  # Cambié esto también