# -*- coding: utf-8 -*-
from flask_admin.contrib.sqla import ModelView
from model.User import User
from model.Asset import Asset
from model.Role import Role
from flask_admin import AdminIndexView, expose
from app import access_required

class HomeView(AdminIndexView):
    @expose('/')
    @access_required('admin')
    def index(self):
        user_model = User()
        role_model = Role()
        asset_model = Asset()

        users = user_model.get_total_users()
        roles = role_model.get_total_roles()
        assets = asset_model.get_total_assets()
    
        return self.render('home_admin.html', report={
            'users': 0 if not users else users[0],
            'roles': 0 if not roles else roles[0],
            'assets': 0 if not assets else assets[0]
        })

class UserView(ModelView):
    column_exclude_list = ['password', 'recovery_code']
    form_excluded_columns = ['last_update', 'recovery_code']

    form_widget_args = {
        'password': {
            'type':'password'
        }
    }

    can_set_page_size = True
    can_view_details = True
    column_searchable_list = ['username', 'email']
    column_filters = ['username', 'email', 'role']
    column_editable_list = ['username', 'email', 'role', 'active']
    create_modal = True
    edit_modal = True
    can_export = True
    column_sortable_list = ['username']
    column_default_sort = ('username', True)
    column_details_exclude_list = ['password', 'recovery_code']
    column_export_exclude_list = ['password', 'recovery_code']
    export_types = ['json', 'yaml', 'csv', 'xls', 'df']

    def on_model_change(self, form, User, is_created):
        if 'password' in form:
            if form.password.data is not None:
                User.set_password(form.password.data)
            else:
                del form.password
    
