import Files
import datetime
import sys
import os
import common
import Locations

def main():
    dataFile = "data/data.json"
    data     = Files.Files().getCurrentJsonDataFromFile(dataFile)
    cities   = []
    
    for city in Locations.cities:    
        cities.append(city["name"]) 
    
    headers   = cities + ["Total", "Mês", "Ano"]
    dataTable = []

    for year, yearValues in data.items():
        for months, monthvalues in yearValues.items():
            dataMonths = []

            for city in Locations.cities:
                ele = list(filter(lambda d: d['id'] == city['id'], monthvalues['data']))
                if len(ele) : 
                    dataMonths.append(ele[0]['text'])
            dataMonths.append((monthvalues['total']))
            dataMonths.append(months)
            dataMonths.append(year)
            dataTable.append(dataMonths)

    markDown = ''

    for h in headers:
        markDown+= " | " + h 
    
    markDown+="\n"

    for h in headers:
        markDown+= " | - "

    markDown+="\n"

    for d in dataTable:
        for v in d:
            markDown+= " | " + str(v) 
        markDown+="\n"

    with open("data/data.md", 'wb') as f:
        f.write(markDown.encode('utf8'))

    return 0  

if __name__ == '__main__':
    sys.exit(main()) 