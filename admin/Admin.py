# -*- coding: utf-8 -*-
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from admin import Views
from model.Asset import Asset
from model.Role import Role
from model.User import User
from model.Market import Market
from model.AssetInfo import AssetInfo

def start_views(app, db):
    admin = Admin(app, name='Meus Ativos', template_mode='bootstrap3',  index_view=Views.HomeView())
    admin.add_view(ModelView(Market, db.session, "Mercado"))
    admin.add_view(ModelView(Role, db.session, "Funções",
    category="Usuários"))
    admin.add_view(Views.UserView(User, db.session, "Usuários", 
    category="Usuários"))
    admin.add_view(ModelView(Asset, db.session, "Ativos", category="Ativos"))
    admin.add_view(ModelView(AssetInfo, db.session, "Atributos", category="Ativos"))
