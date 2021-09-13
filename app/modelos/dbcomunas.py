from app import mysql
class ComunasDB():
    
    def __init__(self):
        car = True


    def buscaComuna(self,idcomu):
        try:
            self.liscomu =[]
            _conn = mysql.connect()
            _cur = _conn.cursor()
            _cur.execute('SELECT * FROM comuna where idComuna = %s',(idcomu))
            _data = _cur.fetchall()
            _conn.commit()
            _conn.close()
            
            for result in _data:
                content = {'id': int(result[0]), 'nombre': str(result[1]),'municipio':int(result[2])}
                self.liscomu.append(content)
            return True
            
        except:
            return False

    def buscaComunas(self):
        try:
            self.liscomus =[]
            _conn = mysql.connect()
            _cur = _conn.cursor()
            _cur.execute('SELECT * FROM comuna')
            _data = _cur.fetchall()
            _conn.commit()
            _conn.close()
            
            for result in _data:
                content = {'id': int(result[0]), 'nombre': str(result[1]),'municipio':int(result[2])}
                self.liscomus.append(content)
            return True
            
        except:
            return False
        
        
    def guardaComuna(self,nombre,munid):
        try:
            conn = mysql.connect()
            cur = conn.cursor()
            oda = (nombre )
            cur.execute('INSERT INTO comuna (nombreComuna,municipioId) VALUES(%s,%s)',(nombre,munid))
        
            conn.commit()
            conn.close()
            return True
        except:
            return False
        
    def deleteComuna(self,id):
        try:
            conn = mysql.connect()
            cur = conn.cursor()
            cur.execute('DELETE FROM comuna WHERE idComuna = %s',(id))
        
            conn.commit()
            conn.close()
            return True
        except:
            return False
    def actualizarComuna(self,nombre,id):
        
            conn = mysql.connect()
            cur = conn.cursor()
            cur.execute('UPDATE comuna SET nombreComuna = %s WHERE idComuna = %s',(nombre,id))
        
            conn.commit()
            conn.close()
            return True
      
       