from app import mysql
class CordenadasDB():
    
    def __init__(self):
        car = True
        
    def guardaCordenadas(self,lat,longi,ente,idn):
        try:
            conn = mysql.connect()
            cur = conn.cursor()
            
            cur.execute('INSERT INTO cordenadas (latitud,longitud,ente,identidicdor) VALUES(%s,%s,%s,%s)',(lat,longi,ente,idn))
        
            conn.commit()
            conn.close()
            return True
        except:
            return False
        
   