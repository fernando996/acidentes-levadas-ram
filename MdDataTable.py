import Files
import datetime
import sys
import os
import common


def main():
    dataFile = "data/data.json"
    data     = Files.Files().getCurrentJsonDataFromFile(dataFile)
    
    cities = [ "Calheta", "Câmara de Lobos", "Funchal", "Machico", "Ponta do Sol",
                "Porto Moniz", "Porto Santo", "Ribeira Brava", "Santa Cruz",
                "Santana", "São Vicente"]
    
    headers = [ "Calheta", "Câmara de Lobos", "Funchal", "Machico", "Ponta do Sol",
                "Porto Moniz", "Porto Santo", "Ribeira Brava", "Santa Cruz",
                "Santana", "São Vicente", "Ano", "Mês"]
    dataTable = []

    for year, yearValues in data.items():
        for months, monthvalues in yearValues.items():
            dataMonths = []

            for city in cities:
                ele = list(filter(lambda d: d['name'] == city, monthvalues['data']))
                

                if len(ele) : 
                    dataMonths.append(ele[0]['text'])
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

    print(markDown)



    return 0  

if __name__ == '__main__':
    sys.exit(main()) 