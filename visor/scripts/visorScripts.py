from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import os

def convert_pdf_to_txt(path, fromPage, toPage):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = toPage
    caching = True
    pagenos=set()
    
    pageIterator = 0
    for page in PDFPage.get_pages(fp, pagenos, maxpages, password=password,caching=caching, check_extractable=True):
        if pageIterator >= fromPage and pageIterator < toPage:
            interpreter.process_page(page)
        
        pageIterator = pageIterator + 1
        if pageIterator == toPage:
            print("salir", pageIterator)
            break

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text

def findFilePath(fileName, path):
    for root, dirs, files in os.walk(path):
        if fileName in files:
            return os.path.join(root, fileName)

def loadOnDemand(targetFile, fromPage, toPage):
    """
    pages are loaded by 10
    """
    print("desde hasta: " , fromPage, toPage)
    data = convert_pdf_to_txt(targetFile, fromPage, toPage)
    return parserData(data)


def parserData(data):
    parsedData = data.replace("\n", "<br>")
    parsedData = parsedData.split("\f", 10)
    parsedData.pop()
    return parsedData  