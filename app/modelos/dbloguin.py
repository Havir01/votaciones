from app import mysql
from werkzeug.security import generate_password_hash,check_password_hash

class LoguinDb():
    
    def __init__(self):
        car = True


    def buscauser(self,cc,passw):
        
        _conn = mysql.connect()
        _cur = _conn.cursor()
        _cur.execute('SELECT ccUsuario,passw,rolid FROM usuarios WHERE ccUsuario=%s',(cc))
        _data = _cur.fetchone()
        _conn.commit()
        _conn.close()
        if _data:
            pw = check_password_hash(_data[1],passw)
            if pw:
                content = {'usuario': int(_data[0]),'rol':int(_data[2])}
                return dict(messaje = "OK",data=content )
            else:
                 return dict(messaje = "PASSWORD INCORRECTO",data=None )

        else:
            return dict(messaje = "USUARIO INCORRECTO",data=None )
        
        
       