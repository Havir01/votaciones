from flask import jsonify
from flask_restful import Resource,request
from app.auth import auth
from app  import app, token_serializer
from app.modelos.dbbarrios import BarriosDB

class Barrios(Resource):
    decorators = [auth.login_required]
    def __init__(self):
        self.barrios = BarriosDB()

    def get(self,user):
        print(user)
        print(auth.current_user())
        if int(user) == int(auth.current_user().get('user')):
            if self.barrios.buscaBarrios():
                _list =  self.barrios.lisbars
                if len(_list) > 0:
                    return jsonify(_list)
                else:
                    return dict(message = "no encontrado")

            else:
                return dict(message = "error")
        else:
            return dict(message = "no register")
class Barrio(Resource):
    decorators = [auth.login_required]
    def __init__(self):
        self.barrios = BarriosDB()

    
    def get(self,user,idba):

        if int(user) == int(auth.current_user().get('user')):
            if self.barrios.buscaBarrio(idba):
                _list =  self.barrios.lisbar
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
        _comuid = request.get_json().get('comuid')
        
        print(request.get_json())
        if int(_user) == int(auth.current_user().get('user')):
            if self.barrios.guardaBarrio(_nombre,_comuid):
                res = dict(messaje= "guardado con exito")
                return res,201
            else:
                return dict(message = "error")
        else:
            res = dict(messaje= "usuario no autorizado")
            return res,400
    def delete(self,user,idba):
        
       
        if int(user) == int(auth.current_user().get('user')):
            if self.barrios.deleteBarrio(idba):
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
            if self.barrios.actualizarBarrio(_nombre,_id):
                res = dict(messaje= "actulizado con exito")
                return res,201
            else:
                return dict(message = "error")
        else:
            res = dict(messaje= "usuario no autorizado")
            return res,400

            

