from flask import session
from controller.User import UserController
from model.Role import Role
from app import access_required

from flask import (
    render_template,
    request,
    redirect,
    Blueprint
)

user_blueprint = Blueprint('user_app', __name__)


@user_blueprint.route('/client_page/', methods=['GET'])
@access_required('client')
def client_area():
    return 'Área do Cliente'

@user_blueprint.route('/promo_page/', methods=['GET'])
def promo_area():
    return '''
        Torne-se um cliente da InvestSys.
        Somos uma casa de análise especializada 
        em pessoa física. E temos relatórios para todos os gostos,
        que usam uma linguagem descomplicada, voltada para leigos.
        Temos relatórios fundamentalistas e análises grafistas em tempo
        real. Entre em contato: comercial@investsysfin.com.
    '''

@user_blueprint.route('/login/', methods=['GET'])
def login():
    return render_template('login.html')

@user_blueprint.route('/login/', methods=['POST'])
def login_post():
    user = UserController()
    role = Role()
    email = request.form['email']
    password = request.form['password']
    result = user.login(email, password)
    if result:
        myrole = role.get_role_by_id(result.role)
        session['role'] = myrole.name
        if result.active:
            if myrole.name == 'admin':
                return redirect('/admin')
            elif myrole.name == "client":
                return redirect('/client_page/')
        else:
            return render_template('login.html', data = {'status':401,
                        'msg':'O usuário especificado foi desativado!',
                        'type': None})
    else:
        return render_template('login.html', data = {'status':401,
                                'msg':'Dados de usuário incorretos',
                                'type': None})

@user_blueprint.route('/recovery_password')
def send_recovery_password():
    user = UserController()
    result = user.recovery(request.form('email'))
    if result:
        return render_template('recovery.html', data={
            'status':200,
            'msg':'email de recuperação enviado com sucesso'
        })
    else:
        return render_template('recovery.html', data={
            'status':401,
            'msg':'Erro ao enviar email de recuperação'
            })
