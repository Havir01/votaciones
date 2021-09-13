from flask import jsonify
from flask_restful import Resource,request
from app.auth import auth
from app  import app, token_serializer
from app.modelos.dbloguin import LoguinDb
from app.modelos.dbdepartamentos import DepartamentosDB

class Departamento(Resource):
    decorators = [auth.login_required]
    def __init__(self):
        self.depar = DepartamentosDB()

    def get(self,user):
        print("entro a depart")
        print(user)
        print(auth.current_user())
        if int(user) == int(auth.current_user().get('user')):
            if self.depar.buscaDepartamentos():
                _list =  self.depar.lisdeps
                if len(_list) > 0:
                    return jsonify(_list)
                else:
                    return dict(message = "no encontrado")

            else:
                return dict(message = "error")
        else:
            return dict(message = "no register")
class Departamentos(Resource):
    decorators = [auth.login_required]
    def __init__(self):
        self.depar = DepartamentosDB()

    
    def get(self,user,idd):
        print("entro a depart")
        print(user)
        print(auth.current_user())
        if int(user) == int(auth.current_user().get('user')):
            if self.depar.buscaDepartamento(idd):
                _list =  self.depar.lisdep
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
        print("guarda guardadepartamento")
       
        if int(_user) == int(auth.current_user().get('user')):
            if self.depar.guardadepartamento(_nombre):
                res = dict(messaje= "guardado con exito")
                return res,201
            else:
                return dict(message = "error")
        else:
            res = dict(messaje= "usuario no autorizado")
            return res,400
    def delete(self,user,id):
        
        print("eliminar departamento")
       
        if int(user) == int(auth.current_user().get('user')):
            if self.depar.deletedepartamento(id):
                res = dict(messaje= "eliminado con exito")
                return res,201
            else:
                 return dict(message = "error")
        else:
            res = dict(messaje= "usuario no autorizado")
            return res,400
    def put(self):
        
        print("actulizar departamento ")
        _user = request.get_json().get('user')
        _id = request.get_json().get('id')
        _nombre = request.get_json().get('nombre')
       
        if int(_user) == int(auth.current_user().get('user')):
            if self.depar.actualizardepartamento(_nombre,_id):
                res = dict(messaje= "actulizado con exito")
                return res,201
            else:
                return dict(message = "error")
        else:
            res = dict(messaje= "usuario no autorizado")
            return res,400

            

