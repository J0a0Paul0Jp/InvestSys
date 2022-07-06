from model.Role import Role
import hashlib, base64, json, jwt
from datetime import datetime, timedelta
from app import app_config, app_active

config = app_config[app_active]

class RoleController():
    def __init__(self):
        self.role_model = Role()