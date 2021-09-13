from app import mysql
class PuestoDB():
    
    def __init__(self):
        car = True


    def buscaPuesto(self,idp):
         try:
            self.lispue =[]
            _conn = mysql.connect()
            _cur = _conn.cursor()
            _cur.execute('SELECT * FROM puestovotacion where idpuesto = %s',(idp))
            _data = _cur.fetchall()
            _conn.commit()
            _conn.close()
            
            for result in _data:
                content = {'id': int(result[0]), 'nombre': str(result[1]),'direccion':str(result[2]),'municipio':int(result[3])}
                self.lispue.append(content)
            return True
         except:
            return False    
        

    def buscaPuestos(self):
        try:
            self.lispues =[]
            _conn = mysql.connect()
            _cur = _conn.cursor()
            _cur.execute('SELECT * FROM puestovotacion')
            _data = _cur.fetchall()
            _conn.commit()
            _conn.close()
            
            for result in _data:
                content = {'id': int(result[0]), 'nombre': str(result[1]),'direccion':str(result[2]),'municipio':str(result[3])}
                self.lispues.append(content)
            return True
        except:
            return False   
            
       
        
    def guardaPuesto(self,nombre,dire,munid):
        try:
            conn = mysql.connect()
            cur = conn.cursor()
            cur2 = conn.cursor()
            oda = (nombre )
            cur.execute('INSERT INTO puestovotacion (nombre,direccion,municipioid) VALUES(%s,%s,%s)',(nombre,dire,munid))
            cur2.execute('select last_insert_id()')
            self.zid = cur2.fetchone()
            conn.commit()
            conn.close()
            return True
        except:
            return False
        
    def deletePuesto(self,id):
        try:
            conn = mysql.connect()
            cur = conn.cursor()
            cur.execute('DELETE FROM puestovotacion WHERE idpuesto = %s',(id))
        
            conn.commit()
            conn.close()
            return True
        except:
            return False
    def actualizarPuesto(self,nombre,dire,munid,idpuesto):
        try:
            conn = mysql.connect()
            cur = conn.cursor()
            cur.execute('UPDATE puestovotacion SET nombre = %s,direccion = %s,municipioid = %s WHERE idpuesto = %s',(nombre,dire,munid,idpuesto))
        
            conn.commit()
            conn.close()
            return True
        except:
            return False
       
       