import Files
import datetime
import zipfile

files = Files.Files('zip')

years  = [2013,2014,2015,2016,2017,2018,2019,2020]
months = ["01","02","03","04","05","06","07","08","09","10","11","12"]

def countTotal(parts):
    total = 0
    for i in parts:
        total+= i["text"] 

    return total


for i in years:
    filename = "zip"+str(i)+".zip"
    date = str(i)+"-01-01"
    format_str = '%Y-%m-%d'  
    date = datetime.datetime.strptime(date, format_str)      
    # url   = files.downloadFileFromUrl(date, filename)

for i in years[2:]:
    filename = "zip"+str(i)+".zip"
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall("zips/"+filename)

    for j in months:
        _file     = "/al_"+str(j)+"_"+str(i)+".pdf"
        _filename = "zips/"+filename+_file
        parts = files.readPdfContent(_filename)
        total = countTotal(parts)
        # data  = files.getCurrentJsonDataFromFile(dataFile)
        # year  = date.strftime("%Y")
        # month = date.strftime("%m")
        print(parts)
    # 

