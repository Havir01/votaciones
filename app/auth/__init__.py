from flask_httpauth import HTTPTokenAuth
from app import token_serializer


auth = HTTPTokenAuth(scheme='Bearer')

@auth.verify_token
def veryfy_token(token):
    print("entra a verificar")
    try:
        data = token_serializer.loads(token)
        print(data)
        if data:
            return data
        else:
            print("no esta en db")
            return False     
    except:
        return False