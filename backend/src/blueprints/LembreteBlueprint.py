from flask import Blueprint, request, jsonify
import logging
from datetime import datetime
from repository.LembreteRepository import LembreteRepository

from flask_jwt_extended import jwt_required, get_jwt_identity

from service.LembreteService import LembreteService

lembretes = Blueprint("lembretes", __name__)

@lembretes.route("/api/lembrete", methods=['GET', 'POST', 'PUT', 'DELETE'])
@jwt_required()
def lembrete():
    usuario_atual = get_jwt_identity()
    
    logging.info(f'Rota /api/lembrete acessada pelo usuario {usuario_atual}.')

    if request.method == 'GET':
        id_lembrete = request.args.get('id')
        try:
            return jsonify(LembreteService.get_by_id(id_lembrete))
        except AssertionError as error:
            logging.error(f'Erro ao obter lembrete por ID: {error}')
            return str(error), 400
    
    if request.method == 'POST':
        data = request.json

        criacao = datetime.now()
        visualizacao = None
        status = True
        id_secretaria = data.get('id_secretaria', 'NOT_FOUND')
        destinatario_cargo = data.get('destinatario_cargo', 'NOT_FOUND')
        destinatario_id = data.get('destinatario_id', 'NOT_FOUND')
        titulo = data.get('titulo', 'NOT_FOUND')
        mensagem = data.get('mensagem', 'NOT_FOUND')
        

        try:
            logging.info(f'Lembrete registrado pelo usuario {usuario_atual}.')

            return LembreteService.register(criacao=criacao, status=status, id_secretaria=id_secretaria,  destinatario_cargo=destinatario_cargo, destinatario_id=destinatario_id, titulo=titulo, mensagem=mensagem)
        except AssertionError as error:
            logging.error(f'Erro ao registrar lembrete: {error}')
            return str(error), 400
    
    if request.method == 'PUT':
        id_lembrete = request.args.get('id')
        data = request.json
        
        status = True
        id_secretaria = data.get('id_secretaria', 'NOT_FOUND')
        destinatario_cargo = data.get('destinatario_cargo', 'NOT_FOUND')
        destinatario_id = data.get('destinatario_id', 'NOT_FOUND')
        titulo = data.get('titulo', 'NOT_FOUND')
        mensagem = data.get('mensagem', 'NOT_FOUND')
        visualizacao = data.get('visualizacao', None)
        criacao = data.get('criacao', None)
        
        try:
            logging.info(f'Lembrete editado pelo usuario {usuario_atual}.')

            return LembreteService.update(id_lembrete=id_lembrete, id_secretaria=id_secretaria, status=status, destinatario_cargo=destinatario_cargo, destinatario_id=destinatario_id, titulo=titulo, mensagem=mensagem, visualizacao=visualizacao, criacao=criacao)
        except AssertionError as error:
            logging.error(f'Erro ao editar lembrete por ID: {error}')
            return str(error), 400
    
    if request.method == 'DELETE':
        id_lembrete = request.args.get('id')
        try:
            logging.info(f'Lembrete deletado pelo usuario {usuario_atual}.')

            return jsonify(LembreteService.delete(id_lembrete))
        except AssertionError as error:
            logging.error(f'Erro ao deletar lembrete por ID: {error}')
            return str(error), 400
    
@lembretes.route("/api/lembrete/listAll", methods=['GET'])
@jwt_required()
def list_all():
    logging.info('Rota /api/lembrete/listAll acessada.')

    return LembreteRepository.lista_all()

@lembretes.route("/api/lembrete/findLembrete", methods=['GET'])
@jwt_required()
def find_lembrete():
    logging.info('Rota /api/lembrete/findLembrete acessada.')

    cargo = request.args.get('cargo')
    id = request.args.get('id')
    try:
        return LembreteService.find_lembrete(cargo, id)
    except AssertionError as error:
        logging.error(f'Erro ao procurar lembrete por ID e cargo: {error}')
        return str(error), 400
    
@lembretes.route("/api/lembrete/visualizar", methods=['PUT'])
@jwt_required()
def lembrete_visualizado():
    usuario_atual = get_jwt_identity()

    logging.info(f'Rota /api/lembrete/visualizar acessada pelo usuario {usuario_atual}.')

    id_lembrete = request.args.get('id')
    try: 
        logging.info(f'Lembrete visualizado pelo usuario {usuario_atual}.')
        return LembreteService.lembrete_visualizado(id_lembrete)
    except AssertionError as error:
        logging.error(f'Erro ao visualizar lembrete: {error}')
        return str(error), 400
    
@lembretes.route("/api/lembrete/visualizados", methods=['GET'])
@jwt_required()
def lembretes_visualizados():
    logging.info('Rota /api/lembrete/visualizados acessada.')

    try:
        return LembreteRepository.lembretes_visualizados()
    except AssertionError as error:
        logging.error(f'Erro ao obter lembretes visualizados: {error}')
        return str(error), 400
    