import requests
import Locations as locations
import Url
import datetime
from PyPDF2 import PdfReader
import json

date = datetime.date(2023, 1, 25)

url = Url.getUrlForDownload(date)
r   = requests.get(url, stream=True)

with open('./metadata.pdf', 'wb') as f:
    f.write(r.content)

reader = PdfReader("metadata.pdf")
page = reader.pages[0]


parts = []
index = 0
ySize = []

def visitor_body(text, cm, tm, font_dict, font_size):
    global index
    global ySize
    # print(text)
    # print(textPos)
    # print(cm)
    # print(tm)
    texts = list(filter(None, text.split()))
    for t in texts:
        if t.isdigit():
            if len(ySize) == 0: 
                ySize.append(int(t))
            elif ySize[-1] == int(t) or ySize[-1] > int(t)  :
                if len(parts)< len(locations.cities):
                    parts.append({'text':int(t), **locations.cities[index] })
                    index+=1
            else:
                ySize.append(int(t))

page.extract_text(visitor_text=visitor_body)

data = None

total = 0 

for i in parts:
    total+= i["text"] 

try:
    with open('./data.json', 'r') as f:
        data = json.load(f)
except:
  print("An exception occurred opening json file") 

year  = date.strftime("%Y")
month = date.strftime("%m")

if (year in data) is False :
    data[year] = {}

data[year][month] = {"data":parts, "total":total, "url":url} 

with open('./data.json', 'w') as f:
    json.dump(data, f)
