import Url
import requests
from PyPDF2 import PdfReader
import Locations
import json

class Files:
    parts = []
    index = 0
    ySize = []

    def downloadFileFromUrl(self, date, filename):
        url = Url.getUrlForDownload(date)
        r   = requests.get(url, stream=True)

        
        with open(filename, 'wb') as f:
            f.write(r.content)
        
        return url

    def readPdfContent(self, filename):
        reader = PdfReader(filename)
        page = reader.pages[0]
        page.extract_text(visitor_text=self.visitor_body)

        return self.parts

    def visitor_body(self, text, cm, tm, font_dict, font_size):
        text = text.replace("0", "0 ")

        texts = list(filter(None, text.split()))
        
        for t in texts:
            if t.isdigit() and t!="2022":
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

