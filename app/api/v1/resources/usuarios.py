from flask import jsonify
from flask_restful import Resource,request
from app.auth import auth
from app  import app, token_serializer
from app.modelos.dbusuarios import UsuariosDB
from app.modelos.dbpersonas import PersonasDB
from app.api.v1.georef import getCordenadas

class Usuarios(Resource):
    decorators = [auth.login_required]
    def __init__(self):
        self.usuario = UsuariosDB()

    def get(self,user):
        print(user)
        print(auth.current_user())
        
        if int(user) == int(auth.current_user().get('user')):
            if self.usuario.buscaUsuarios():
                _list =  self.usuario.lisusers
                if len(_list) > 0:
                    return jsonify(_list)
                else:
                    return dict(message = "no encontrado")

            else:
                return dict(message = "error")
        else:
            return dict(message = "no register")
class Usuario(Resource):
    decorators = [auth.login_required]
    def __init__(self):
        self.personas = PersonasDB()
        self.usuario = UsuariosDB()

    
    def get(self,user,cc):

        if int(user) == int(auth.current_user().get('user')):
            if self.usuario.buscaUsuario(cc):
                _list =  self.usuario.lisuser
                if len(_list) > 0:
                    return jsonify(_list)
                else:
                    return dict(message = "no encontrado")

            else:
                return dict(message = "error")
        else:
            return dict(message = "no register")
    
    def post(self):
        _user = request.get_json().get('user')
        _cc = request.get_json().get('cc')
        _passw = request.get_json().get('passw')
        _rolid = request.get_json().get('rolid')
        
        
        print(request.get_json())
        if int(_user) == int(auth.current_user().get('user')):
            if self.usuario.guardaUsuario(_cc,_passw,_rolid):
                if int(_rolid) == 1:
                    ult = self.usuario.zid
                    self.personas.buscaPersona(_cc)
                    usr = self.personas.lisper[0]
                    dire = usr.get("direccion")
                    barrio = usr.get("barrio")
                    ciudad = usr.get("ciudad")
                    busq = str(dire) +", "+ str(barrio) +", "+ str(ciudad) 
                    getCordenadas(busq,"lider",ult)
                res = dict(messaje= "guardado con exito")
                return res,201
            else:
                return dict(message = "error")
        else:
            res = dict(messaje= "usuario no autorizado")
            return res,400
    def delete(self,user,cc):
        
       
        if int(user) == int(auth.current_user().get('user')):
            if self.usuario.deleteUsuario(cc):
                res = dict(messaje= "eliminado con exito")
                return res,201
            else:
                 return dict(message = "error")
        else:
            res = dict(messaje= "usuario no autorizado")
            return res,400
    