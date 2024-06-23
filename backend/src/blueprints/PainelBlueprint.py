from flask import Blueprint, request, jsonify
import logging
from datetime import datetime
from repository.PainelRepository import PainelRepository
from dtos.PainelDTO import PainelDTO
from service.PainelService import PainelService

from flask_jwt_extended import jwt_required, get_jwt_identity

paineis = Blueprint("painel", __name__)

@paineis.route("/api/painel", methods=['GET', 'POST', 'PUT', 'DELETE'])
@jwt_required()
def painel():
    usuario_atual = get_jwt_identity()
    logging.info(f'Rota /api/painel acessada pelo usuario {usuario_atual}.')
    if request.method == 'GET':
        id_painel = request.args.get('id')
        try:
            return jsonify(PainelService.get_by_id(id_painel))
        except AssertionError as error:
            logging.error(f'Erro ao obter painel por ID: {error}')
            return str(error), 400
    
    if request.method == 'POST':
        data = request.json

        data_criado = datetime.now()
        status = True
        id_configuracao = data.get('id_configuracao', 'NOT_FOUND')
        id_secretaria = data.get('id_secretaria', 'NOT_FOUND')
        total_ativo = data.get('total_ativo', 'NOT_FOUND')
        total_presentes = data.get('total_presentes', 'NOT_FOUND')
        total_ausentes = data.get('total_ausentes', 'NOT_FOUND')
        total_presentes_curso = data.get('total_presentes_curso', 'NOT_FOUND')
        total_ativo_curso = data.get('total_ativo_curso', 'NOT_FOUND')
        total_ausente_curso = data.get('total_ausente_curso', 'NOT_FOUND')

        print(data)
        try:
            logging.info(f'Painel com id {id_secretaria} registrado pelo usuario {usuario_atual}.')

            return PainelService.register(id_configuracao=id_configuracao, id_secretaria=id_secretaria, total_ativo=total_ativo, total_ausentes=total_ausentes, total_presentes=total_presentes, total_presentes_curso=total_presentes_curso, total_ativo_curso=total_ativo_curso, total_ausente_curso=total_ausente_curso, status=status, data_criado=data_criado)
        except AssertionError as error:
            logging.error(f'Erro ao registrar painel: {error}')
            return str(error), 400
    
    if request.method == 'PUT':
        id_painel = request.args.get('id')
        data = request.json

        data_criado = datetime.now()
        status = True
        id_configuracao = data.get('id_configuracao', 'NOT_FOUND')
        id_secretaria = data.get('id_secretaria', 'NOT_FOUND')
        total_ativo = data.get('total_ativo', 'NOT_FOUND')
        total_presentes = data.get('total_presentes', 'NOT_FOUND')
        total_ausentes = data.get('total_ausentes', 'NOT_FOUND')
        total_presentes_curso = data.get('total_presentes_curso', 'NOT_FOUND')
        total_ativo_curso = data.get('total_ativo_curso', 'NOT_FOUND')
        total_ausente_curso = data.get('total_ausente_curso', 'NOT_FOUND')

        try:
            logging.info(f'Painel com id {id_painel} editado pelo usuario {usuario_atual}.')

            return PainelService.update(id_painel=id_painel, id_configuracao=id_configuracao, id_secretaria=id_secretaria, total_ativo=total_ativo, total_ausentes=total_ausentes, total_presentes=total_presentes, total_presentes_curso=total_presentes_curso, total_ativo_curso=total_ativo_curso, total_ausente_curso=total_ausente_curso, status=status, data_criado=data_criado)
        except AssertionError as error:
            logging.error(f'Erro ao editar painel por ID: {error}')
            return str(error), 400
        
    if request.method == 'DELETE':
        id_painel = request.args.get('id')
        try:
            logging.info(f'Painel com id {id_painel} deletado pelo usuario {usuario_atual}.')

            return jsonify(PainelService.delete(id_painel))
        except AssertionError as error:
            logging.error(f'Erro ao deletar painel por ID: {error}')
            return str(error), 400
    
@paineis.route("/api/painel/listAll", methods=['GET'])
@jwt_required()
def list_all():
    logging.info('Rota /api/painel acessada.')
    return PainelRepository.list_all()