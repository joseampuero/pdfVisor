from django.http import JsonResponse
from visor.scripts import translatorScripts, visorScripts
from visor.serializers import textSerializer
from visor.models import Text
import constants

def visor(request, file, fromPage, toPage):
    pdfPath = visorScripts.findFilePath(file, constants.ROOT_PATH)
    print("el path es ", pdfPath)

    text = visorScripts.loadOnDemand(pdfPath, fromPage, toPage)
    textToLoad = Text(text, fromPage, toPage)
    textSerialized = textSerializer.TextSerializer(textToLoad)

    return JsonResponse(textSerialized.data)

def translator(request, sentence):
    return translatorScripts.translate(sentence)