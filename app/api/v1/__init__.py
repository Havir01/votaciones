from flask_restful import Api
from app import app

api = Api(app)



from app.api.v1.resources.loguin import Loguin
from app.api.v1.resources.departamentos import Departamentos,Departamento
from app.api.v1.resources.municipios import Municipio,Municipios
from app.api.v1.resources.comunas import Comuna,Comunas
from app.api.v1.resources.barrios import Barrio,Barrios
from app.api.v1.resources.personas import Persona,Personas
from app.api.v1.resources.usuarios import Usuario,Usuarios
from app.api.v1.resources.puesto import Puesto,Puestos
from app.api.v1.resources.votantes import Votante,VotantesXlider,VotantesXmunicipios,VotantesXpuesto,Votantes,VotantesXthislider


api.add_resource(Loguin,'/api/v1/loguin')
api.add_resource(Departamentos,'/api/v1/departamentos/<int:user>/<int:idd>','/api/v1/guardadepartamento','/api/v1/deletedepartamento/<int:user>/<int:id>','/api/v1/actualizardepartamento')
api.add_resource(Departamento,'/api/v1/departamentos/<int:user>')

api.add_resource(Municipios,'/api/v1/<int:user>/municipios')
api.add_resource(Municipio,'/api/v1/<int:user>/municipios/<int:idm>','/api/v1/guardamunicipio','/api/v1/<int:user>/deletemunicipio/<int:idm>','/api/v1/actualizarmunicipio')

api.add_resource(Comunas,'/api/v1/<int:user>/comunas')
api.add_resource(Comuna,'/api/v1/<int:user>/comunas/<int:idco>','/api/v1/guardacomuna','/api/v1/<int:user>/deletecomuna/<int:idc>','/api/v1/actualizarcomuna')

api.add_resource(Barrios,'/api/v1/<int:user>/barrios')
api.add_resource(Barrio,'/api/v1/<int:user>/barrios/<int:idba>','/api/v1/guardabarrio','/api/v1/<int:user>/deletebarrio/<int:idba>','/api/v1/actualizarbarrio')

api.add_resource(Personas,'/api/v1/<int:user>/personas')
api.add_resource(Persona,'/api/v1/<int:user>/personas/<int:cc>','/api/v1/guardapersona','/api/v1/<int:user>/deletepersona/<int:cc>','/api/v1/actualizarpersona')

api.add_resource(Usuarios,'/api/v1/<int:user>/usuarios')
api.add_resource(Usuario,'/api/v1/<int:user>/usuarios/<int:cc>','/api/v1/guardausuario','/api/v1/<int:user>/deleteusuario/<int:cc>')

api.add_resource(Puestos,'/api/v1/<int:user>/puestos')
api.add_resource(Puesto,'/api/v1/<int:user>/puestos/<int:idp>','/api/v1/guardapuesto','/api/v1/<int:user>/deletepuesto/<int:idp>','/api/v1/actualizarpuesto')

api.add_resource(Votantes,'/api/v1/<int:user>/votantes')
api.add_resource(VotantesXlider,'/api/v1/<int:user>/votantes/lider/<int:idli>')
api.add_resource(VotantesXthislider,'/api/v1/<int:user>/votantes/thislider')
api.add_resource(VotantesXmunicipios,'/api/v1/<int:user>/votantes/municipio/<int:idmu>')
api.add_resource(VotantesXpuesto,'/api/v1/<int:user>/votantes/puesto/<int:idp>')
api.add_resource(Votante,'/api/v1/guardavotante')