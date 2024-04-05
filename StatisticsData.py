
import Files
import datetime
import sys
import os

def countTotal(parts):
    total = 0
    for i in parts:
        total+= i["text"] 

    return total

def prepareDataForSaving(year, month, data, parts, total, url):
    if (year in data) is False :
        data[year] = {}

    data[year][month] = {"data":parts, "total":total, "url":url} 

def main():
    inputDate = None 
    date = None

    if len(sys.argv) > 1  : 
        inputDate = sys.argv[1]
        format_str = '%Y-%m-%d'  
        try:
            date = datetime.datetime.strptime(inputDate, format_str)         
        except:
            print("Invalid date format") 
            return 1
    else :
        date = datetime.datetime.now()

    filename = "metadata.pdf"
    dataFile = "data.json"

    files = Files.Files()
    url   = files.downloadFileFromUrl(date, filename)
    parts = files.readPdfContent(filename)
    total = countTotal(parts)
    data  = files.getCurrentJsonDataFromFile(dataFile)
    year  = date.strftime("%Y")
    month = date.strftime("%m")

    prepareDataForSaving(year, month, data, parts, total, url)

    files.setJsonToFile(dataFile, data)
    
    os.remove(filename)

    return 0  

if __name__ == '__main__':
    sys.exit(main()) 