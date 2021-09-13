from app import mysql
class PersonasDB():
    
    def __init__(self):
        car = True


    def buscaPersona(self,cc):
        try:
            self.lisper =[]
            _conn = mysql.connect()
            _cur = _conn.cursor()
            _cur.execute('''SELECT ccPersona,nombres,apellidos,direccion,cel,barrio.nombreBarrio,comuna.nombreComuna,municipio.nombreMunicipio
                        FROM personas INNER JOIN barrio ON personas.barrio = barrio.idBarrio 
                        INNER JOIN comuna ON personas.comuna = comuna.idComuna 
                        INNER JOIN municipio ON personas.ciudad=municipio.idMunicipio 
                        where ccPersona = %s''',(cc))
            _data = _cur.fetchall()
            _conn.commit()
            _conn.close()
            
            for result in _data:
                content = {'cc': int(result[0]), 'nombres': str(result[1]),'apellidos': str(result[2]),'direccion':str(result[3]),'cel':str(result[4]),'barrio':str(result[5]),'comuna':str(result[6]),'ciudad':str(result[7])}
                self.lisper.append(content)
            return True
            
        except:
            return False

    def buscaPersonas(self):
        try:
            self.lispers =[]
            _conn = mysql.connect()
            _cur = _conn.cursor()
            _cur.execute('SELECT * FROM personas')
            _data = _cur.fetchall()
            _conn.commit()
            _conn.close()
            
            for result in _data:
                content = {'cc': int(result[0]), 'nombres': str(result[1]),'apellidos': str(result[2]),'direccion':str(result[3]),'cel':str(result[4])}
                self.lispers.append(content)
            return True
            
        except:
            return False
        
        
    def guardaPersona(self,cc,nombres,apellidos,direccion,celular):
        try:
            conn = mysql.connect()
            cur = conn.cursor()
            
            cur.execute('INSERT INTO personas (ccPersona,nombres,apellidos,direccion,cel) VALUES(%s,%s,%s,%s,%s)',(cc,nombres,apellidos,direccion,celular))
        
            conn.commit()
            conn.close()
            return True
        except:
            return False
        
    def deletePersona(self,cc):
        try:
            conn = mysql.connect()
            cur = conn.cursor()
            cur.execute('DELETE FROM personas WHERE ccPersona = %s',(cc))
        
            conn.commit()
            conn.close()
            return True
        except:
            return False
    def actualizarPersona(self,nombres,apellidos,direccion,celular,cc):
        
            conn = mysql.connect()
            cur = conn.cursor()
            cur.execute('UPDATE personas SET nombres = %s, apellidos = %s, direccion = %s, cel = %s WHERE ccPersona = %s',(nombres,apellidos,direccion,celular,cc))
        
            conn.commit()
            conn.close()
            return True
      
       