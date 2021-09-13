from app import mysql
from werkzeug.security import generate_password_hash,check_password_hash
class UsuariosDB():
    
    def __init__(self):
        car = True


    def buscaUsuario(self,cc):
        try:
            self.lisuser =[]
            _conn = mysql.connect()
            _cur = _conn.cursor()
            _cur.execute('SELECT ccUsuario,rolid,nombres,apellidos,direccion FROM usuarios INNER JOIN personas ON usuarios.ccUsuario = personas.ccPersona  WHERE usuarios.ccUsuario = %s',(cc))
            _data = _cur.fetchall()
            _conn.commit()
            _conn.close()
            
            for result in _data:
                content = {'cc': int(result[0]), 'rol': int(result[1]),'nombres': str(result[2]),'apellidos':str(result[3]),'direccion':str(result[4])}
                self.lisuser.append(content)
            return True
            
        except:
            return False

    def buscaUsuarios(self):
        try:
            self.lisusers =[]
            _conn = mysql.connect()
            _cur = _conn.cursor()
            _cur.execute('SELECT ccUsuario,rolid,nombres,apellidos,direccion FROM usuarios INNER JOIN personas ON usuarios.ccUsuario = personas.ccPersona')
            _data = _cur.fetchall()
            _conn.commit()
            _conn.close()
            
            for result in _data:
                content = {'cc': int(result[0]), 'rol': int(result[1]),'nombres': str(result[2]),'apellidos':str(result[3]),'direccion':str(result[4])}
                self.lisusers.append(content)
            return True
            
        except:
            return False
        
        
    def guardaUsuario(self,cc,passw,rolid):
        
        try:
            conn = mysql.connect()
            cur = conn.cursor()
            cur2 = conn.cursor()
            paswencrip = generate_password_hash(str(passw),method="sha256")
            cur.execute('INSERT INTO usuarios (ccUsuario,passw,rolid) VALUES(%s,%s,%s)',(cc,paswencrip,rolid))
            cur2.execute('select last_insert_id()')
            self.zid = cur2.fetchone()
            conn.commit()
            conn.close()
            return True
        except:
            return False
    def deleteUsuario(self,cc):
        try:
            conn = mysql.connect()
            cur = conn.cursor()
            cur.execute('DELETE FROM usuarios WHERE ccUsuario = %s',(cc))
        
            conn.commit()
            conn.close()
            return True
        except:
            return False
    