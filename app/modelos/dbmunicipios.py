from app import mysql
class MunicipiosDB():
    
    def __init__(self):
        car = True


    def buscaMunicipio(self,idm):
        try:
            self.lismun =[]
            _conn = mysql.connect()
            _cur = _conn.cursor()
            _cur.execute('SELECT * FROM municipio where idMunicipio = %s',(idm))
            _data = _cur.fetchall()
            _conn.commit()
            _conn.close()
            
            for result in _data:
                content = {'id': int(result[0]), 'nombre': str(result[1]),'departamento':int(result[2])}
                self.lismun.append(content)
            return True
            
        except:
            return False

    def buscaMunicipios(self):
        try:
            self.lismuns =[]
            _conn = mysql.connect()
            _cur = _conn.cursor()
            _cur.execute('SELECT * FROM municipio')
            _data = _cur.fetchall()
            _conn.commit()
            _conn.close()
            
            for result in _data:
                content = {'id': int(result[0]), 'nombre': str(result[1]),'departamento':int(result[2])}
                self.lismuns.append(content)
            return True
            
        except:
            return False
        
        
    def guardaMunicipio(self,nombre,depid):
        try:
            conn = mysql.connect()
            cur = conn.cursor()
            oda = (nombre )
            cur.execute('INSERT INTO municipio (nombreMunicipio,depId) VALUES(%s,%s)',(nombre,depid))
        
            conn.commit()
            conn.close()
            return True
        except:
            return False
        
    def deleteMunicipio(self,id):
        try:
            conn = mysql.connect()
            cur = conn.cursor()
            cur.execute('DELETE FROM municipio WHERE idMunicipio = %s',(id))
        
            conn.commit()
            conn.close()
            return True
        except:
            return False
    def actualizarMunicipio(self,nombre,id):
        try:
            conn = mysql.connect()
            cur = conn.cursor()
            cur.execute('UPDATE municipio SET nombreMunicipio = %s WHERE idMunicipio = %s',(nombre,id))
        
            conn.commit()
            conn.close()
            return True
        except:
            return False
       