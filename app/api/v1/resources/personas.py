from flask import jsonify
from flask_restful import Resource,request
from app.auth import auth
from app  import app, token_serializer
from app.modelos.dbpersonas import PersonasDB

class Personas(Resource):
    decorators = [auth.login_required]
    def __init__(self):
        self.person = PersonasDB()

    def get(self,user):
        print(user)
        print(auth.current_user())
        if int(user) == int(auth.current_user().get('user')):
            if self.person.buscaPersonas():
                _list =  self.person.lispers
                if len(_list) > 0:
                    return jsonify(_list)
                else:
                    return dict(message = "no encontrado")

            else:
                return dict(message = "error")
        else:
            return dict(message = "no register")
class Persona(Resource):
    decorators = [auth.login_required]
    def __init__(self):
        self.person = PersonasDB()

    
    def get(self,user,cc):

        if int(user) == int(auth.current_user().get('user')):
            if self.person.buscaPersona(cc):
                _list =  self.person.lisper
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
        _nombres = request.get_json().get('nombres')
        _apellidos = request.get_json().get('apellidos')
        _direccion = request.get_json().get('direccion')
        _cel = request.get_json().get('cel')
        
        print(request.get_json())
        if int(_user) == int(auth.current_user().get('user')):
            if self.person.guardaPersona(_cc,_nombres,_apellidos,_direccion,_cel):
                res = dict(messaje= "guardado con exito")
                return res,201
            else:
                return dict(message = "error")
        else:
            res = dict(messaje= "usuario no autorizado")
            return res,400
    def delete(self,user,cc):
        
       
        if int(user) == int(auth.current_user().get('user')):
            if self.person.deletePersona(cc):
                res = dict(messaje= "eliminado con exito")
                return res,201
            else:
                 return dict(message = "error")
        else:
            res = dict(messaje= "usuario no autorizado")
            return res,400
    def put(self):
        _user = request.get_json().get('user')
        _cc = request.get_json().get('cc')
        _nombres = request.get_json().get('nombres')
        _apellidos = request.get_json().get('apellidos')
        _direccion = request.get_json().get('direccion')
        _cel = request.get_json().get('cel')
        
        if int(_user) == int(auth.current_user().get('user')):
            if self.person.actualizarPersona(_nombres,_apellidos,_direccion,_cel,_cc):
                res = dict(messaje= "actulizado con exito")
                return res,201
            else:
                return dict(message = "error")
        else:
            res = dict(messaje= "usuario no autorizado")
            return res,400

            