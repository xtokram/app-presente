from flask import Blueprint, request, jsonify
import logging
from repository.MateriaRepository import MateriaRepository
from flask_jwt_extended import jwt_required, get_jwt_identity
from service.MateriaService import MateriaService

from utils import oidc

materias = Blueprint("Materia", __name__)   

@materias.route("/api/materia", methods=['GET', 'POST','PUT','DELETE'])
@jwt_required()
# @oidc.accept_token()
def materia():
    usuario_atual = get_jwt_identity()

    logging.info(f'Rota /api/materia acessada pelo usuario {usuario_atual}.')
    if request.method == 'GET':
        id_materia = request.args.get('id')
        try:    
            return jsonify(MateriaService.get_by_id(id_materia))
        except AssertionError as error:
            logging.error(f'Erro ao obter materia por ID: {error}')
            return str(error), 400
    
    if request.method == 'POST':
        data = request.json
    
        status = True
        nome = data.get('nome', 'NOT_FOUND')

        try:
            logging.info(f'Materia {nome} registrada pelo usuario {usuario_atual}.')

            return MateriaService.register(status=status, nome=nome)
        except AssertionError as error:
            logging.error(f'Erro ao registrar materia: {error}')
            return str(error), 400
    
    if request.method == 'PUT':
        id_materia = request.args.get('id')
        data = request.json

        status = True
        nome = data.get('nome', 'NOT_FOUND')

        try: 
            logging.info(f'Materia com id {id_materia} editada pelo usuario {usuario_atual}.')

            return MateriaService.update(id_materia=id_materia, status=status, nome=nome)
        except AssertionError as error:
            logging.error(f'Erro ao editar materia por ID: {error}')
            return str(error), 400
    
    if request.method == 'DELETE':
        id_materia = request.args.get('id')
        try:
            logging.info(f'Materia  com id {id_materia} deletada pelo usuario {usuario_atual}.')

            return jsonify(MateriaService.delete(id_materia))
        except AssertionError as error:
            logging.error(f'Erro ao deletar materia por ID: {error}')
            return str(error), 400
    
@materias.route("/api/materia/listAll", methods=['GET'])
@jwt_required()
def listar_all_materias():
    logging.info('Rota /api/materia/listAll acessada.')
    return MateriaRepository.list_all()