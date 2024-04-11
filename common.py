def countTotal(parts):
    total = 0
    for i in parts:
        total+= i["text"] 

    return total

def prepareDataForSaving(year, month, data, parts, total, url):
    if (year in data) is False :
        data[year] = {}

    data[year][month] = {"data":parts, "total":total, "url":url}
