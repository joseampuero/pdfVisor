from django.http import JsonResponse
from visor.scripts import translatorScripts, visorScripts

def visor(request, file):
    print("llego el llamado", file)
    pdfPath = visorScripts.findFilePath(file, "/home/jose/Documentos")
    print("el path es ", pdfPath)

    text = visorScripts.convert_pdf_to_txt(pdfPath)
    parsedText = text.replace("\n", "<br>")
    
    return JsonResponse({"text": parsedText})

def translator(request, sentence):
    return translatorScripts.translate(sentence)