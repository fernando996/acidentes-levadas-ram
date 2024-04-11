
import Files
import datetime
import sys
import os
import common

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
    dataFile = "data/data.json"

    files = Files.Files()
    url   = files.downloadFileFromUrl(date, filename)
    parts = files.readPdfContent(filename)
    total = common.countTotal(parts)
    data  = files.getCurrentJsonDataFromFile(dataFile)
    year  = date.strftime("%Y")
    month = date.strftime("%m")

    common.prepareDataForSaving(year, month, data, parts, total, url)

    files.setJsonToFile(dataFile, data)
    
    os.remove(filename)

    return 0  

if __name__ == '__main__':
    sys.exit(main()) 