from model.User import User
import hashlib, base64, json, jwt
from datetime import datetime, timedelta
from app import app_config, app_active

config = app_config[app_active]

class UserController():
    def __init__(self):
        self.user_model = User()
    
    def verify_auth_token(self, access_token):
        status = 401
        try:
            jwt.decode(access_token, config.SECRET, algorithm='HS256')
            message = 'Token válido'
            status = 200
        except jwt.ExpiredSignatureException:
            message = 'Token expirado, realize um novo login'
        except:
            message = 'Token inválido'
        
        return {
            'message': message,
            'status': status
        }

    def generate_auth_token(self, data, exp=30, time_exp=False):
        if time_exp == True:
            date_time = data['exp']
        else:
            date_time = datetime.utcnow() + timedelta(minutes=exp)
        
        dict_jwt = {
            'id': data['id'],
            'username': data['username'],
            'exp': date_time
        }

        access_token = jwt.encode(dict_jwt, config.SECRET, algorithm='HS256')
        return access_token

    def login(self, email, password):
        self.user_model.email = email
        result = self.user_model.get_user_by_email()
        print(result)
        if result is not None:
            res = self.user_model.verify_password(password, result.password)
            if res:
                return result
            else:
                return {}
        return {}

    def recovery(email):
        return ''

