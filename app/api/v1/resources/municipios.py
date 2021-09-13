from flask import jsonify
from flask_restful import Resource,request
from app.auth import auth
from app  import app, token_serializer
from app.modelos.dbmunicipios import MunicipiosDB

class Municipios(Resource):
    decorators = [auth.login_required]
    def __init__(self):
        self.muni = MunicipiosDB()

    def get(self,user):
        print("entro a municipios")
        print(user)
        print(auth.current_user())
        if int(user) == int(auth.current_user().get('user')):
            if self.muni.buscaMunicipios():
                _list =  self.muni.lismuns
                if len(_list) > 0:
                    return jsonify(_list)
                else:
                    return dict(message = "no encontrado")

            else:
                return dict(message = "error")
        else:
            return dict(message = "no register")
class Municipio(Resource):
    decorators = [auth.login_required]
    def __init__(self):
        self.muni = MunicipiosDB()

    
    def get(self,user,idm):
        print("entro a depart")
        print(user)
        print(auth.current_user())
        if int(user) == int(auth.current_user().get('user')):
            if self.muni.buscaMunicipio(idm):
                _list =  self.muni.lismun
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
        _depid = request.get_json().get('depid')
        
       
        if int(_user) == int(auth.current_user().get('user')):
            if self.muni.guardaMunicipio(_nombre,_depid):
                res = dict(messaje= "guardado con exito")
                return res,201
            else:
                return dict(message = "error")
        else:
            res = dict(messaje= "usuario no autorizado")
            return res,400
    def delete(self,user,idm):
        
       
        if int(user) == int(auth.current_user().get('user')):
            if self.muni.deleteMunicipio(idm):
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
            if self.muni.actualizarMunicipio(_nombre,_id):
                res = dict(messaje= "actulizado con exito")
                return res,201
            else:
                return dict(message = "error")
        else:
            res = dict(messaje= "usuario no autorizado")
            return res,400

            

