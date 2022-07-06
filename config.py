import os
import random, string

class Config(object):
    CSRF_ENABLED = True #habilita criptografia
    SECRET = 'ysb_92=qe#djf8%ng+a*#4rt#5%3*4k5%i2bck*gn@w3@f&-&' #criar chaves...
    TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                     'templates') #caminho para o local
                                                  #onde os arquivos de template ficarão
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) #caminho do local onde a raiz                                                            #do projeto se contra
    APP = None #propriedade do app
    SQLALCHEMY_DATABASE_URI = 'sqlite:///investsys.db'
    #Preencha com os dados do seu banco de dados
    # User - Usuário do banco
    # Passwd - Senha do usuário
    # Host - Geralmente no local fica localhost
    # Port - Geralmente 3306 no mysql
    # Database - Nome do banco de dados

class DevelopmentConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 32064
    URL_MAIN = 'http://%s:%s/' % (IP_HOST, PORT_HOST)

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = 'localhost' # Aqui geralmente é um IP de um servidor na
    #nuvem e não o endereço da máquina local
    PORT_HOST = 32064
    URL_MAIN = 'http://%s:%s/' % (IP_HOST, PORT_HOST)

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    IP_HOST = 'loca' # Aqui geralmente é um IP de um servidor na
    #nuvem e não o endereço da máquina local
    PORT_HOST = 32064
    URL_MAIN = 'http://%s:%s/' % (IP_HOST, PORT_HOST)

app_config = {
    'development': DevelopmentConfig(),
    'testing': TestingConfig(),
    'production': ProductionConfig()
}

app_active = os.getenv('FLASK_ENV')

