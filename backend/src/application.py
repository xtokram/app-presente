from flask import Flask
from flask_cors import CORS
from models import login_manager
import logging
import json_log_formatter
import warnings
from sqlalchemy import exc as sqlalchemy_exc

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
            logging.FileHandler("/home/ubuntu/presente-backend/backend/src/backend.log"),
            logging.StreamHandler()
        ]             
    )

    formatter = json_log_formatter.JSONFormatter()

    json_handler = logging.FileHandler('/home/ubuntu/presente-backend/backend/src/backend.log')
    json_handler.setFormatter(formatter)

    logger = logging.getLogger('json_logger')
    logger.addHandler(json_handler)
    logger.setLevel(logging.INFO)


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

    
    db.init_app(app)
    
    
    login_manager.init_app(app)
    app.logger.info('Aplicativo inicializado com sucesso.')

    return app





