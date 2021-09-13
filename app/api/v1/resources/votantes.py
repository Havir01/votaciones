from flask import jsonify
from flask_restful import Resource,request
from app.auth import auth
from app  import app, token_serializer
from app.modelos.dbusuarios import UsuariosDB
from app.modelos.dbpersonas import PersonasDB
from app.modelos.dbvotantes import VotantesDB
from app.api.v1.georef import getCordenadas

class Votantes(Resource):
    decorators = [auth.login_required]
    def __init__(self):
        self.votante = VotantesDB()

    def get(self,user):
        print(user)
        print(auth.current_user())
        
        if int(user) == int(auth.current_user().get('user')) and int(auth.current_user().get('rol'))==2:
            if self.votante.buscaVotantes():
                _list =  self.votante.lisvon
                if len(_list) > 0:
                    return jsonify(_list)
                else:
                    return dict(message = "no encontrado")

            else:
                return dict(message = "error")
        else:
            return dict(message = "no autorizado")
class VotantesXlider(Resource):
    decorators = [auth.login_required]
    def __init__(self):
        self.votante = VotantesDB()

    def get(self,user,idli):
        print(user)
        print(auth.current_user())
        
        if int(user) == int(auth.current_user().get('user')) and int(auth.current_user().get('rol'))==2:
            if self.votante.buscaVotanteXlider(idli):
                _list =  self.votante.lislid
                if len(_list) > 0:
                    return jsonify(_list)
                else:
                    return dict(message = "no encontrado")

            else:
                return dict(message = "error")
        
        else:
            return dict(message = "no autorizado")
class VotantesXthislider(Resource):
    decorators = [auth.login_required]
    def __init__(self):
        self.votante = VotantesDB()

    def get(self,user):
        print(user)
        print(auth.current_user())
        
        if int(user) == int(auth.current_user().get('user')) and int(auth.current_user().get('rol'))==1:
            if self.votante.buscaVotanteXlider(user):
                _list =  self.votante.lislid
                if len(_list) > 0:
                    return jsonify(_list)
                else:
                    return dict(message = "no encontrado")

            else:
                return dict(message = "error")
        
        else:
            return dict(message = "no autorizado")
        
class VotantesXmunicipios(Resource):
    decorators = [auth.login_required]
    def __init__(self):
        self.votante = VotantesDB()

    def get(self,user,idmu):
        print(user)
        print(auth.current_user())
        
        if int(user) == int(auth.current_user().get('user')) and int(auth.current_user().get('rol'))==2:
            if self.votante.buscaVotanteXmunicipio(idmu):
                _list =  self.votante.lismun
                if len(_list) > 0:
                    return jsonify(_list)
                else:
                    return dict(message = "no encontrado")

            else:
                return dict(message = "error")
        else:
            return dict(message = "no autorizado")
class VotantesXpuesto(Resource):
    decorators = [auth.login_required]
    def __init__(self):
        self.votante = VotantesDB()

    def get(self,user,idp):
        print(user)
        print(auth.current_user())
        
        if int(user) == int(auth.current_user().get('user')) and int(auth.current_user().get('rol'))==2:
            if self.votante.buscaVotanteXpuesto(idp):
                _list =  self.votante.lispuest
                if len(_list) > 0:
                    return jsonify(_list)
                else:
                    return dict(message = "no encontrado")

            else:
                return dict(message = "error")
        else:
            return dict(message = "no register")
class Votante(Resource):
    decorators = [auth.login_required]
    def __init__(self):
        self.votante = VotantesDB()

    
    def get(self,user,cc):

        if int(user) == int(auth.current_user().get('user')) and int(auth.current_user().get('rol'))==2:
            if self.usuario.buscaUsuario(cc):
                _list =  self.usuario.lisuser
                if len(_list) > 0:
                    return jsonify(_list)
                else:
                    return dict(message = "no encontrado")

            else:
                return dict(message = "error")
        else:
            return dict(message = "no autorizado")
    
    def post(self):
        _user = request.get_json().get('user')
        _perosonacc = request.get_json().get('cc')
        _liderId = request.get_json().get('liderId')
        _barrioId = request.get_json().get('barrioId')
        _puestoVotaId = request.get_json().get('puestoVotaId')
        _mesa = request.get_json().get('mesa')
        
        
        print(request.get_json())
        if int(_user) == int(auth.current_user().get('user')) and int(auth.current_user().get('rol'))==1:
            if self.votante.guardaVotantes(_perosonacc,_liderId,_barrioId,_puestoVotaId,_mesa):
                return dict(message = "guardado con exito")
            else:
                return dict(message = "error")
        else:
            res = dict(messaje= "usuario no autorizado")
            return res,400
    