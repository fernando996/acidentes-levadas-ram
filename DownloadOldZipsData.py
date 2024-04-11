import Files
import datetime
import zipfile
import os
import Url

years  = [2016,2017,2018,2019,2020]
# years  = [2013,2014,2015,2016,2017,2018,2019,2020]
months = ["01","02","03","04","05","06","07","08","09","10","11","12"]

def countTotal(parts):
    total = 0
    for i in parts:
        total+= i["text"] 

    return total

def prepareDataForSaving(year, month, data, parts, total, url):
    if (year in data) is False :
        data[year] = {}

    data[year][month] = {"data":parts, "total":total, "url":url} 

data = {}

files = Files.Files()
dataFile = "zipData.json"
currentDataFile = "data.json"
currentData = files.getCurrentJsonDataFromFile(currentDataFile)

for i in years:
    filename = "zip"+str(i)+".zip"
    date = str(i)+"-01-01"
    format_str = '%Y-%m-%d'  
    date = datetime.datetime.strptime(date, format_str) 

    files = Files.Files('zip')
    # url   = files.downloadFileFromUrl(date, filename)
    url   =  Url.getZipUrlForDownload(date)


    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall("zips/"+filename)
    
    # fix 2020 file
    if i == 2020:
        os.rename('zips/zip2020.zip/al_11_2020..pdf', 'zips/zip2020.zip/al_11_2020.pdf')

    for j in months:
        _file     = "/al_"+str(j)+"_"+str(i)+".pdf"
        _filename = "zips/"+filename+_file

        files = Files.Files('zip')

        parts = files.readPdfContent(_filename, str(i))
        total = countTotal(parts)
    
        year  = i
        month = j

        prepareDataForSaving(year, month, data, parts, total, url)
        files.setJsonToFile(dataFile, data)

        prepareDataForSaving(year, month, currentData, parts, total, url)
        files.setJsonToFile(currentDataFile, currentData)


