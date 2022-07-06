# -*- coding: utf-8 -*-
from re import template
from flask import Flask, redirect, url_for, session, render_template_string
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
#from flask_login import LoginManager
from config import app_config, app_active
from functools import wraps

config = app_config[app_active]
db = None
app = None
auth = None
def create_app(config_name=None):
    global db, app, config, auth
    if config_name is None:
        config_name = app_active
    app = Flask(__name__, template_folder='templates')
    app.secret_key = config.SECRET
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    config = app_config[app_active]
    config.APP = app
    db = SQLAlchemy(config.APP)
    Bootstrap(app)
    db.init_app(app)
#    login_manager = LoginManager()
#    login_manager.init_app(app)
    from model import Role, User, Market, Asset, AssetInfo, AssetTrail, AssetTrailInfo
    from admin.Admin import start_views
    from blueprints.User import user_blueprint
    migrate = Migrate(app, db)
    app.register_blueprint(user_blueprint)
    migrate.init_app(app, db)
    start_views(app, db)
    return app

def access_required(role="any"):
    """
    see: https://flask.palletsprojects.com/en/2.1.x/patterns/viewdecorators/
    """
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if session.get("role") == None or role == "any":
                session['header'] = "Welcome Guest, Request a new role for higher rights!"
                return redirect('/promo_page/')
            if session.get("role") == 'client' and role == 'client':
                print("access: Client")
                session['header'] = "Welcome to Client Page!"
            elif session.get("role") == 'admin' and role == 'admin':
                session['header'] = "Welcome to Admin Page!"
                print("access: Admin")
            else:
                session['header'] = "Oh no no, you haven'tn right of access!!!"
                return redirect('/login/')
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper
