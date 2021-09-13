from flask import jsonify
from flask_restful import Resource,request
from app.auth import auth
from app  import app, token_serializer
from app.modelos.dbloguin import LoguinDb

class Loguin(Resource):
    def __init__(self):
        self.usuario = LoguinDb()
        
    def post(self):
        print("entro a lohin")
        _user = request.get_json().get('user') 
        _pass = request.get_json().get('pass')
        print(request.get_json()) 
        _resp = self.usuario.buscauser(_user,_pass)
        print(_resp)
        
        if _resp.get('data'):
            _rol = _resp.get('data').get('rol')
            token = token_serializer.dumps(dict(user = _user,rol=_rol)).decode('utf-8')
            data = {"estado":"AUTORIZADO","toquen":token}
            return data,201
        else:
            data = {"estado":"NO-AUTORIZADO"}
            return data,400