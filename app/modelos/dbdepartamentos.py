from app import mysql


class DepartamentosDB():
    
    def __init__(self):
        car = True


    def buscaDepartamento(self,idd):
        try:
            self.lisdep =[]
            _conn = mysql.connect()
            _cur = _conn.cursor()
            _cur.execute('SELECT * FROM departamentos where idDepartamento = %s',(idd))
            _data = _cur.fetchall()
            _conn.commit()
            _conn.close()
            
            for result in _data:
                content = {'id': int(result[0]), 'nombre': str(result[1])}
                self.lisdep.append(content)
            return True
            
        except:
            return False

    def buscaDepartamentos(self):
        try:
            self.lisdeps =[]
            _conn = mysql.connect()
            _cur = _conn.cursor()
            _cur.execute('SELECT * FROM departamentos')
            _data = _cur.fetchall()
            _conn.commit()
            _conn.close()
            
            for result in _data:
                content = {'id': int(result[0]), 'nombre': str(result[1])}
                self.lisdeps.append(content)
            return True
            
        except:
            return False
        
        
    def guardadepartamento(self,nombre):
        try:
            conn = mysql.connect()
            cur = conn.cursor()
            oda = (nombre )
            cur.execute('INSERT INTO departamentos (nombreDepartamento) VALUES(%s)',(nombre))
        
            conn.commit()
            conn.close()
            return True
        except:
            return False
        
    def deletedepartamento(self,id):
        try:
            conn = mysql.connect()
            cur = conn.cursor()
            cur.execute('DELETE FROM departamentos WHERE idDepartamento = %s',(id))
        
            conn.commit()
            conn.close()
            return True
        except:
            return False
    def actualizardepartamento(self,nombre,id):
        try:
            conn = mysql.connect()
            cur = conn.cursor()
            cur.execute('UPDATE departamentos SET nombreDepartamento = %s WHERE idDepartamento = %s',(nombre,id))
        
            conn.commit()
            conn.close()
            return True
        except:
            return False
       