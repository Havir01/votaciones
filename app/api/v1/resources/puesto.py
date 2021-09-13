from flask import jsonify
from flask_restful import Resource,request
from app.auth import auth
from app  import app, token_serializer
from app.modelos.dbpuesto import PuestoDB
from app.modelos.dbmunicipios import MunicipiosDB
from app.api.v1.georef import getCordenadas

class Puestos(Resource):
    decorators = [auth.login_required]
    def __init__(self):
        self.puesto = PuestoDB()

    def get(self,user):
        
        print(user)
        print(auth.current_user())
        if int(user) == int(auth.current_user().get('user')):
            if self.puesto.buscaPuestos():
                _list =  self.puesto.lispues
                if len(_list) > 0:
                    return jsonify(_list)
                else:
                    return dict(message = "no encontrado")

            else:
                return dict(message = "error")
        else:
            return dict(message = "no register")
class Puesto(Resource):
    decorators = [auth.login_required]
    def __init__(self):
        self.puesto = PuestoDB()
        self.muni = MunicipiosDB()
    
    def get(self,user,idp):
        
        print(auth.current_user())
        if int(user) == int(auth.current_user().get('user')):
            if self.puesto.buscaPuesto(idp):
                _list =  self.puesto.lispue
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
        _dire = request.get_json().get('dire')
        _munid= request.get_json().get('munid')
        
       
        if int(_user) == int(auth.current_user().get('user')):
            if self.puesto.guardaPuesto(_nombre,_dire,_munid):
                ult = self.puesto.zid
                self.muni.buscaMunicipio(_munid)
                ciudad = self.muni.lismun[0].get("nombre")
                busq = str(_nombre) + ", "+ str(ciudad) 
                getCordenadas(busq,"puesto",ult)
                res = dict(messaje= "guardado con exito")
                return res,201
            else:
                return dict(message = "error")
        else:
            res = dict(messaje= "usuario no autorizado")
            return res,400
    def delete(self,user,idp):
        
       
        if int(user) == int(auth.current_user().get('user')):
            if self.puesto.deletePuesto(idp):
                res = dict(messaje= "eliminado con exito")
                return res,201
            else:
                 return dict(message = "error")
        else:
            res = dict(messaje= "usuario no autorizado")
            return res,400
    def put(self):
        
        _user = request.get_json().get('user')
        _nombre = request.get_json().get('nombre')
        _dire = request.get_json().get('dire')
        _munid= request.get_json().get('munid')
        _idpuesto = request.get_json().get('idpuesto')
       
        if int(_user) == int(auth.current_user().get('user')):
            if self.puesto.actualizarPuesto(_nombre,_dire,_munid,_idpuesto):
                res = dict(messaje= "actulizado con exito")
                return res,201
            else:
                return dict(message = "error")
        else:
            res = dict(messaje= "usuario no autorizado")
            return res,400

            

