from app import mysql
class VotantesDB():
    
    def __init__(self):
        car = True


    def buscaVotanteXlider(self,idlider):
         try:
            self.lislid =[]
            _conn = mysql.connect()
            _cur = _conn.cursor()
            _cur.execute('''SELECT personas.ccPersona,personas.nombres,personas.apellidos,personas.direccion,barrio.nombreBarrio,comuna.nombreComuna,puestovotacion.nombre AS puesto,votante.liderId 
                           FROM votante INNER JOIN personas ON votante.perosonacc = personas.ccPersona 
                           INNER JOIN barrio ON personas.barrio = barrio.idBarrio 
                           INNER JOIN comuna ON barrio.comunaId = comuna.idComuna 
                           INNER JOIN puestovotacion ON votante.puestoVotaId = puestovotacion.idpuesto 
                           INNER JOIN usuarios ON votante.liderId = usuarios.ccUsuario 
                           WHERE usuarios.ccUsuario = %s''',(idlider))
            
            _data = _cur.fetchall()
            _conn.commit()
            _conn.close()
            
            for result in _data:
                content = {'cc': int(result[0]), 'nombres': str(result[1]),'apellidos':str(result[2]),'direccion':str(result[3]),'barrio':str(result[4]),'comuna':str(result[5]),'puesto':str(result[6]),'lider':str(result[7])}
                self.lislid.append(content)
            return True
         except:
            return False
    def buscaVotanteXmunicipio(self,idmun):
         try:
            self.lismun =[]
            _conn = mysql.connect()
            _cur = _conn.cursor()
            _cur.execute('''SELECT personas.ccPersona,personas.nombres,personas.apellidos,personas.direccion,barrio.nombreBarrio,comuna.nombreComuna,puestovotacion.nombre AS puesto,votante.liderId 
                         FROM votante INNER JOIN personas ON votante.perosonacc = personas.ccPersona 
                         INNER JOIN barrio ON personas.barrio = barrio.idBarrio 
                         INNER JOIN comuna ON barrio.comunaId = comuna.idComuna 
                         INNER JOIN puestovotacion ON votante.puestoVotaId = puestovotacion.idpuesto 
                         INNER JOIN usuarios ON votante.liderId = usuarios.ccUsuario 
                         WHERE comuna.municipioId = %s''',(idmun))
            _data = _cur.fetchall()
            _conn.commit()
            _conn.close()
            
            for result in _data:
                content = {'cc': int(result[0]), 'nombres': str(result[1]),'apellidos':str(result[2]),'direccion':str(result[3]),'barrio':str(result[4]),'comuna':str(result[5]),'puesto':str(result[6]),'lider':str(result[7])}
                self.lismun.append(content)
            return True
         except:
            return False        
        
    def buscaVotanteXpuesto(self,idpuesto):
         try:
            self.lispuest =[]
            _conn = mysql.connect()
            _cur = _conn.cursor()
            _cur.execute('''SELECT personas.ccPersona,personas.nombres,personas.apellidos,personas.direccion,barrio.nombreBarrio,comuna.nombreComuna,puestovotacion.nombre AS puesto,votante.liderId 
                           FROM votante INNER JOIN personas ON votante.perosonacc = personas.ccPersona 
                           INNER JOIN barrio ON personas.barrio = barrio.idBarrio 
                           INNER JOIN comuna ON barrio.comunaId = comuna.idComuna 
                           INNER JOIN puestovotacion ON votante.puestoVotaId = puestovotacion.idpuesto 
                           INNER JOIN usuarios ON votante.liderId = usuarios.ccUsuario 
                           WHERE votante.puestoVotaId = %s''',(idpuesto))
            
            _data = _cur.fetchall()
            _conn.commit()
            _conn.close()
            
            for result in _data:
                content = {'cc': int(result[0]), 'nombres': str(result[1]),'apellidos':str(result[2]),'direccion':str(result[3]),'barrio':str(result[4]),'comuna':str(result[5]),'puesto':str(result[6]),'lider':str(result[7])}
                self.lispuest.append(content)
            return True
         except:
            return False
    def buscaVotantes(self):
        try:
            self.lisvon =[]
            _conn = mysql.connect()
            _cur = _conn.cursor()
            _cur.execute('''SELECT personas.ccPersona,personas.nombres,personas.apellidos,personas.direccion,barrio.nombreBarrio,comuna.nombreComuna,puestovotacion.nombre AS
                          puesto,votante.liderId 
                          FROM votante INNER JOIN personas ON votante.perosonacc = personas.ccPersona 
                          INNER JOIN barrio ON personas.barrio = barrio.idBarrio 
                          INNER JOIN comuna ON barrio.comunaId = comuna.idComuna 
                          INNER JOIN puestovotacion ON votante.puestoVotaId = puestovotacion.idpuesto 
                          INNER JOIN usuarios ON votante.liderId = usuarios.ccUsuario''')
            _data = _cur.fetchall()
            _conn.commit()
            _conn.close()
            
            for result in _data:
                content = {'cc': int(result[0]), 'nombres': str(result[1]),'apellidos':str(result[2]),'direccion':str(result[3]),'barrio':str(result[4]),'comuna':str(result[5]),'puesto':str(result[6]),'lider':str(result[7])}
                self.lisvon.append(content)
            return True
        except:
            return False   
            
       
        
    def guardaVotantes(self,perosonacc,liderId,barrioId,puestoVotaId,mesa):
        try:
            conn = mysql.connect()
            cur = conn.cursor()
            cur2 = conn.cursor()
            
            cur.execute('INSERT INTO votante (perosonacc,liderId,barrioId,puestoVotaId,mesa) VALUES(%s,%s,%s,%s,%s)',(perosonacc,liderId,barrioId,puestoVotaId,mesa))
            cur2.execute('select last_insert_id()')
            self.zid = cur2.fetchone()
            conn.commit()
            conn.close()
            return True
        except:
            return False    
    