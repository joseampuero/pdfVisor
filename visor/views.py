from django.shortcuts import render
from django.http import JsonResponse
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import os

def visor(request, file):
    print("llego el llamado", file)
    pdfPath = findFilePath(file, "/home/jose/Documentos")
    print("el path es ", pdfPath)

    # pdfPath = "/home/jose/Documentos/books/Chip Heath, Dan Heath - Made to Stick_ Why Some Ideas Survive and Others Die.pdf"
    text = convert_pdf_to_txt(pdfPath)
    return JsonResponse({"saludo": "respuesta desde el back"})

def findFilePath(fileName, path):
    for root, dirs, files in os.walk(path):
        if fileName in files:
            return os.path.join(root, fileName)

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text