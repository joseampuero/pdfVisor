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
    # Dividir por páginas primero (separador \f)
    parsedData = data.split("\f")
    parsedData = [page for page in parsedData if page.strip()]  # Remover páginas vacías
    
    # Convertir cada página a párrafos HTML clickeables
    pages_with_paragraphs = []
    
    for page_index, page in enumerate(parsedData):
        # Dividir por saltos de línea dobles (párrafos reales)
        paragraphs = page.split("\n\n")
        
        # Crear HTML con párrafos clickeables
        html_paragraphs = []
        for paragraph_index, paragraph in enumerate(paragraphs):
            if paragraph.strip():
                # Limpiar saltos de línea simples dentro del párrafo
                clean_paragraph = paragraph.replace("\n", " ").strip()
                # Crear párrafo con ID único y clase clickeable
                paragraph_id = f"page-{page_index}-paragraph-{paragraph_index}"
                html_paragraphs.append(
                    f'<p class="clickable-paragraph" data-paragraph-id="{paragraph_id}">{clean_paragraph}</p>'
                )
        
        pages_with_paragraphs.append("".join(html_paragraphs))
    
    return pages_with_paragraphs