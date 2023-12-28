import math
import sys
import os 
import json 
from visor.scripts import storageScripts

CONTENT_KEY = "content"
MAX_SIZE_KB = 24

def learningHandler(fromPage, toPage):
    data = get_content(fromPage, toPage)
    draw_up(data)
    # connect_GPT()

def get_current_index(target_index):
    return target_index % 10 - 1

def get_current_file_index(target_index):
    return math.floor(target_index/10) * 10

def get_content(fromPage, toPage):
    fromPageFileIndex = get_current_file_index(fromPage)
    toPageFileIndex = get_current_file_index(toPage)

    fromPageIndex = get_current_index(fromPage)
    toPageIndex = get_current_index(toPage)

    targetFileNames = [f"{num}.json" for num in list(range(fromPageFileIndex, toPageFileIndex + 1, 10))]

    dataToLearn = []

    data = os.listdir(storageScripts.FOLDER_PATH)
    content = []
    for currentFileName in targetFileNames:
        if currentFileName in data:
            filePath = os.path.join(storageScripts.FOLDER_PATH, currentFileName)
            with open(filePath, 'r') as file:
                fileContent = json.load(file)
                
                if CONTENT_KEY in fileContent:
                    if currentFileName == targetFileNames[0]:
                        content = fileContent[CONTENT_KEY][-fromPageIndex:]
                    elif currentFileName == targetFileNames[-1]:  
                        content = fileContent[CONTENT_KEY][:toPageIndex]
                    else:
                        content = fileContent[CONTENT_KEY]
                    dataToLearn.extend(content)

    return content

def draw_up(pages):
    # is a set of pages that does not exceed the maximum size in kb
    virtualPage = [] 
    # is a set of virtual pages
    virtualChapter = []
    virtualPageSize = 0

    for aPage in pages:
        # in bytes
        currentPageSize = sys.getsizeof(aPage)

        if virtualPageSize + currentPageSize <= MAX_SIZE_KB * 1000:
            virtualPage.append(aPage)
            virtualPageSize += currentPageSize
        else:
            virtualChapter.append(virtualPage)
            virtualPage = [aPage]
            virtualPageSize = currentPageSize
    
    if virtualPage:
        virtualChapter.append(virtualPage)
    
    
