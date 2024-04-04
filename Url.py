import datetime

URL = 'http://www.procivmadeira.pt/images/dispositivo-socorro/acidentes-percursos-terrestres/al_'

def getUrlForDownload(date):
    if isinstance(date, datetime.date) is False:
        raise Exception("The date parameter is not a valid date object!")
    return URL + date.strftime("%m_%Y") + ".pdf"