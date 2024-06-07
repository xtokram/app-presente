from flask import Flask
from flask_cors import CORS
from models import login_manager
import logging
from json_log_formatter import JSONFormatter
import warnings
from sqlalchemy import exc as sqlalchemy_exc
from flask_session import Session
import redis

class CustomJSONFormatter(JSONFormatter):
    def json_record(self, message, extra, record):
        extra['log.level'] = record.levelname.lower()
        extra['@timestamp'] = self.format_time(record.created)
        extra['log.logger'] = record.name
        extra['log.origin'] = {
            'function': record.funcName,
            'file.name': record.pathname,
            'file.line': record.lineno,
        }
        extra['message'] = record.getMessage()
        extra['service.name'] = 'flask_app'
        extra['ecs.version'] = '1.6.0'
        return extra

def create_app(config_file):
    
    warnings.filterwarnings("ignore", category=sqlalchemy_exc.SAWarning)

    from models import db
    from flask_login import LoginManager
    from blueprints.AlunoBlueprint import alunos
    from blueprints.ChamadaBlueprint import chamadas
    from blueprints.LembreteBlueprint import lembretes
    from blueprints.PainelBlueprint import paineis
    from blueprints.PresencaBlueprint import presencas
    from blueprints.ProfessorBlueprint import professores
    from blueprints.SecretariaBlueprint import secretaria
    from blueprints.MateriaBlueprint import materias
    from blueprints.TurmaBlueprint import turmas
    from blueprints.UsuarioBlueprint import usuarios
    from blueprints.ConfiguracaoBlueprint import configuracoes
    from flask_wtf.csrf import CSRFProtect
    from flask_jwt_extended import JWTManager


    app = Flask(__name__)
    CORS(app)
    # CSRFProtect(app)
    
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.FileHandler("backend.log"),
            logging.StreamHandler()
        ]             
    )

    formatter = CustomJSONFormatter()

    json_handler = logging.FileHandler('backend.log')
    json_handler.setFormatter(formatter)

    json_logger = logging.getLogger('json_logger')
    json_logger.addHandler(json_handler)
    json_logger.setLevel(logging.INFO)


    app.config.from_pyfile(config_file)   

    jwt = JWTManager(app)

    app.register_blueprint(alunos)
    app.register_blueprint(chamadas)
    app.register_blueprint(lembretes)
    app.register_blueprint(paineis)
    app.register_blueprint(presencas)
    app.register_blueprint(professores)
    app.register_blueprint(secretaria)
    app.register_blueprint(materias)
    app.register_blueprint(turmas)
    app.register_blueprint(usuarios)
    app.register_blueprint(configuracoes)


    # Configuração da sessão com Redis
    app.config['SESSION_TYPE'] = 'redis'
    app.config['SESSION_PERMANENT'] = False
    app.config['SESSION_USE_SIGNER'] = True
    app.config['SESSION_KEY_PREFIX'] = "session:" 
    app.config['SESSION_REDIS'] = redis.Redis(
        host=app.config['REDIS_HOST'],
        port=app.config['REDIS_PORT'],
        password=app.config['REDIS_PASSWORD']
    )

    Session(app)
    
    db.init_app(app)
    
    
    login_manager.init_app(app)
    app.logger.info('Aplicativo inicializado com sucesso.')

    return app