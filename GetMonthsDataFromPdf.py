import Files
import datetime
import common
from PyPDF2 import PdfWriter, PdfReader
import os

# The year of 2021 has the data on the same pdf
years  = [2021]
months = ["01","02","03","04","05","06","07","08","09","10","11","12"]

data = {}

files = Files.Files()
dataFile="2021.json"
currentDataFile = "data/data.json"
currentData = files.getCurrentJsonDataFromFile(currentDataFile)
pdfDir = "pdf"
for i in years:
    filename = "Ano"+str(i)+".pdf"
    date = str(i)+"-01-01"
    format_str = '%Y-%m-%d'  
    date = datetime.datetime.strptime(date, format_str) 
    url  = "http://www.procivmadeira.pt/images/dispositivo-socorro/"+ filename

    # Read PDF with all data
    inputpdf = PdfReader(open(filename, "rb"))
    os.mkdir(pdfDir)

    for p in range(len(inputpdf.pages)):
        output = PdfWriter()
        output.add_page(inputpdf.pages[p])
        with open("pdf/%s.pdf" % (p+1), "wb") as outputStream:
            output.write(outputStream)

    for j in months:

        files = Files.Files()
        

        _filename = "pdf/"+ str(j[1] if  j[0] =="0" else j) + ".pdf"

        parts = files.readPdfContent(_filename, str(i), True)
        total = common.countTotal(parts)
    
        year  = i
        month = j

        common.prepareDataForSaving(year, month, data, parts, total, url)
        files.setJsonToFile(dataFile, data)

        common.prepareDataForSaving(year, month, currentData, parts, total, url)
        files.setJsonToFile(currentDataFile, currentData)

dir = os.listdir(pdfDir)
for f in dir:
    os.remove(pdfDir+"/"+f)
os.removedirs(pdfDir)


