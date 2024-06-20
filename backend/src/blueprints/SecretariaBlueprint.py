from flask import Blueprint, request, jsonify
import logging
from repository.SecretariaRepository import SecretariaRepository

from flask_jwt_extended import jwt_required, get_jwt_identify
from service.SecretariaService import SecretariaService

secretaria = Blueprint("secretaria", __name__)

@secretaria.route("/api/secretaria", methods=['GET', 'POST', 'PUT', 'DELETE'])
# @jwt_required()
def secret():
    usuario_atual = get_jwt_identify().get('nome')
    logging.info(f'Rota /api/secretaria acessada pelo usuario {usuario_atual}.')
    if request.method == 'GET':
        id_secretaria = request.args.get('id')
        try:
            return jsonify(SecretariaService.get_by_id(id_secretaria))
        except AssertionError as error:
            logging.error(f'Erro ao obter secretaria por ID: {error}')
            return str(error), 400
        
    if request.method == 'POST':
        data = request.json
        
        status = True
        id_usuario = data.get('id_usuario', 'NOT_FOUND')
        nome = data.get('nome', 'NOT_FOUND')
        
        try:
            logging.info(f'Secretaria registrada pelo usuario {usuario_atual}.')

            return SecretariaService.register(id_usuario=id_usuario, status=status, nome=nome)
        except AssertionError as error:
            logging.error(f'Erro ao registrar secretaria: {error}')
            return str(error), 400
    
    if request.method == 'PUT':
        id_secretaria = request.args.get('id')
        data = request.json
        
        status = True
        id_secretaria = data.get('id_secretaria', 'NOT_FOUND')
        nome = data.get('nome', 'NOT_FOUND')
        
        try:
            logging.info(f'Secretaria editada pelo usuario {usuario_atual}.')

            return SecretariaService.update(id_secretaria=id_secretaria, status=status, nome=nome)
        except AssertionError as error:
            logging.error(f'Erro ao editar secretaria por ID: {error}')
            return str(error), 400
    
    if request.method == 'DELETE':
        id_secretaria = request.args.get('id')
        try:
            logging.info(f'Secretaria deletada pelo usuario {usuario_atual}.')

            return jsonify(SecretariaService.delete(id_secretaria))
        except AssertionError as error:
            logging.error(f'Erro ao deletar secretaria por ID: {error}')
            return str(error), 400 

@secretaria.route("/api/secretaria/listAll", methods=['GET'])
@jwt_required()
def list_all():
    logging.info('Rota /api/secretaria/listAll acessada.')
    return SecretariaRepository.list_all()