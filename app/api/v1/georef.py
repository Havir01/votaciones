import requests
from app.modelos.dbcordenadas import CordenadasDB


def getCordenadas(busq,ente,identificador):
    url = "https://maps.googleapis.com/maps/api/geocode/json?address="+busq+",+CA&key="
    key = "AIzaSyA0c_ylWHHGriUj9P25v9xjafxxcFwwpc8"
    try:
        resp = requests.get(url+str(key))
        cor =resp.json()
        print(cor)
        cordenadas = cor.get("results")[0].get("geometry").get("location")
        lat = cordenadas.get("lat")
        lng= cordenadas.get("lng")
        gcor = CordenadasDB()
        gcor.guardaCordenadas(lat,lng,ente,identificador)
        return True
    except:
        print("error en geolocalalizacion")
        return False
    
    
   