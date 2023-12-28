import os
import json

FOLDER_PATH = "/home/jose/Documentos/skills/pdfVisor/data"

# data is saved so that can be learned by IA
def manageTempData(textSerialized):
    build_folder()

    file_name = "{}/{}.json".format(FOLDER_PATH, textSerialized["fromPage"])
    print(file_name)
    with open(file_name, 'w') as file:
        json.dump(textSerialized, file)

def build_folder():
    if not os.path.exists(FOLDER_PATH):
        os.makedirs(FOLDER_PATH)