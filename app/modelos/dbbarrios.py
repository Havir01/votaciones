from app import mysql
class BarriosDB():
    
    def __init__(self):
        car = True


    def buscaBarrio(self,idba):
        try:
            self.lisbar =[]
            _conn = mysql.connect()
            _cur = _conn.cursor()
            _cur.execute('SELECT * FROM barrio where idBarrio = %s',(idba))
            _data = _cur.fetchall()
            _conn.commit()
            _conn.close()
            
            for result in _data:
                content = {'id': int(result[0]), 'nombre': str(result[1]),'Barrio':int(result[2])}
                self.lisbar.append(content)
            return True
            
        except:
            return False

    def buscaBarrios(self):
        try:
            self.lisbars =[]
            _conn = mysql.connect()
            _cur = _conn.cursor()
            _cur.execute('SELECT * FROM barrio')
            _data = _cur.fetchall()
            _conn.commit()
            _conn.close()
            
            for result in _data:
                content = {'id': int(result[0]), 'nombre': str(result[1]),'Barrio':int(result[2])}
                self.lisbars.append(content)
            return True
            
        except:
            return False
        
        
    def guardaBarrio(self,nombre,comuid):
        try:
            conn = mysql.connect()
            cur = conn.cursor()
            
            cur.execute('INSERT INTO barrio (nombreBarrio,comunaId) VALUES(%s,%s)',(nombre,comuid))
        
            conn.commit()
            conn.close()
            return True
        except:
            return False
        
    def deleteBarrio(self,id):
        try:
            conn = mysql.connect()
            cur = conn.cursor()
            cur.execute('DELETE FROM barrio WHERE idBarrio = %s',(id))
        
            conn.commit()
            conn.close()
            return True
        except:
            return False
    def actualizarBarrio(self,nombre,id):
        
            conn = mysql.connect()
            cur = conn.cursor()
            cur.execute('UPDATE barrio SET nombreBarrio = %s WHERE idBarrio = %s',(nombre,id))
        
            conn.commit()
            conn.close()
            return True
      
       