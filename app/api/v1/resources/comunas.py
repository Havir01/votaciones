from flask import jsonify
from flask_restful import Resource,request
from app.auth import auth
from app  import app, token_serializer
from app.modelos.dbcomunas import ComunasDB

class Comunas(Resource):
    decorators = [auth.login_required]
    def __init__(self):
        self.comunas = ComunasDB()

    def get(self,user):
        print(user)
        print(auth.current_user())
        if int(user) == int(auth.current_user().get('user')):
            if self.comunas.buscaComunas():
                _list =  self.comunas.liscomus
                if len(_list) > 0:
                    return jsonify(_list)
                else:
                    return dict(message = "no encontrado")

            else:
                return dict(message = "error")
        else:
            return dict(message = "no register")
class Comuna(Resource):
    decorators = [auth.login_required]
    def __init__(self):
        self.comunas = ComunasDB()

    
    def get(self,user,idco):
        print("entro a depart")
        print(user)
        print(auth.current_user())
        if int(user) == int(auth.current_user().get('user')):
            if self.comunas.buscaComuna(idco):
                _list =  self.comunas.liscomu
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
        _nombre = request.get_json().get('nombre')
        _munid = request.get_json().get('munid')
        
       
        if int(_user) == int(auth.current_user().get('user')):
            if self.comunas.guardaComuna(_nombre,_munid):
                res = dict(messaje= "guardado con exito")
                return res,201
            else:
                return dict(message = "error")
        else:
            res = dict(messaje= "usuario no autorizado")
            return res,400
    def delete(self,user,idc):
        
       
        if int(user) == int(auth.current_user().get('user')):
            if self.comunas.deleteComuna(idc):
                res = dict(messaje= "eliminado con exito")
                return res,201
            else:
                 return dict(message = "error")
        else:
            res = dict(messaje= "usuario no autorizado")
            return res,400
    def put(self):
        _user = request.get_json().get('user')
        _id = request.get_json().get('id')
        _nombre = request.get_json().get('nombre')
        
        if int(_user) == int(auth.current_user().get('user')):
            if self.comunas.actualizarComuna(_nombre,_id):
                res = dict(messaje= "actulizado con exito")
                return res,201
            else:
                return dict(message = "error")
        else:
            res = dict(messaje= "usuario no autorizado")
            return res,400

            

