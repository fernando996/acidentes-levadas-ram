import Url
import requests
import Locations
import json

from tika import parser # pip install tika

class Files:
    parts   = []
    index   = 0
    ySize   = []
    year    = None
    uriType = 'pdf'

    # default constructor
    def __init__(self, uriType = 'pdf'):
        self.parts   = []
        self.index   = 0
        self.ySize   = []
        self.year    = None
        self.uriType = uriType

    def downloadFileFromUrl(self, date, filename):
        self.year = date.year
        
        url  = Url.getUrlForDownload(date) if  self.uriType == 'pdf' else Url.getZipUrlForDownload(date)
        r    = requests.get(url, stream=True)

        
        with open(filename, 'wb') as f:
            f.write(r.content)
        
        return url

    def readPdfContent(self, filename, year = ''):
        print(filename)
        raw   = parser.from_file(filename)

        spWord = "SRPC, IP-RAM"

        if ".xlsx" in raw['content'] :
            spWord = ".xlsx"   

        if ".pdf" in raw['content'] :
            spWord = ".pdf"
        if ".docx" in raw['content'] :
            spWord = ".docx"    

        text = raw['content'].replace(year, "")
        texts = text.split(spWord)
        self.getData(texts[1])

        return self.parts

    def getData(self, texts) :        
        for t in texts:
            if t.isdigit() :
                if len(self.ySize) == 0: 
                    self.ySize.append(int(t))
                elif self.ySize[-1] == int(t) or self.ySize[-1] > int(t)  :
                    if len(self.parts)< len(Locations.cities):
                        self.parts.append({'text':int(t), **Locations.cities[self.index] })
                        self.index+=1
                else:
                    self.ySize.append(int(t))

    def getCurrentJsonDataFromFile(self, filename): 
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except:
            print("An exception occurred opening json file") 

    def setJsonToFile(self, filename, data): 
        with open(filename, 'w') as f:
            json.dump(data, f)

