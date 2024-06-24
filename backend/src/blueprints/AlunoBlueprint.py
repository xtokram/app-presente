from flask import Blueprint, request, jsonify
import logging
from repository.AlunoRepository import AlunoRepository
from flask_jwt_extended import jwt_required, get_jwt_identity

from service.AlunoService import AlunoService

alunos = Blueprint("alunos", __name__)

@alunos.route("/api/aluno", methods=['GET', 'POST', 'PUT', 'DELETE'])
@jwt_required()
def aluno():
    usuario_atual = get_jwt_identity()

    logging.info(f'Rota /api/aluno acessada pelo usuario {usuario_atual}.')

    if request.method == 'GET':
        id_aluno = request.args.get('id')
        try:
            return jsonify(AlunoService.get_by_id(id_aluno))
        except AssertionError as error:
            logging.error(f'Erro ao obter aluno por ID: {error}')

            return str(error), 400
        
    if request.method == 'POST':    
        data = request.json
        
        id_usuario = data.get('id_usuario', 'NOT_FOUND')
        nome = data.get('nome', 'NOT_FOUND')
        ra = data.get('ra', 'NOT_FOUND')

        status = True
        ausente = False
        
        try:
            logging.info(f'ALUNO_REGISTRADO: Aluno {nome} registrado pelo usuario {usuario_atual}.')

            return AlunoService.register(id_usuario=id_usuario, status=status, nome=nome, ra=ra, ausente=ausente)
        except AssertionError as error:
            logging.error(f'Erro ao registrar aluno por ID: {error}')

            return str(error), 400

    if request.method == 'PUT':
        id_aluno = request.args.get('id')
        data = request.json    

        nome = data.get('nome', 'NOT_FOUND')
        ra = data.get('ra', 'NOT_FOUND')

        status = True
        ausente = False

        try:
            logging.info(f'ALUNO_EDITADO: Aluno {nome} editado pelo usuario {usuario_atual}.')

            return AlunoService.update(id_aluno=id_aluno, status=status, nome=nome, ra=ra, ausente=ausente)
        except AssertionError as error:
            logging.error(f'Erro ao editar aluno por ID: {error}')

            return str(error), 400
        
    if request.method == 'DELETE':
        id_aluno = request.args.get('id')
        try:
            logging.info(f'ALUNO_DELETADO: Aluno com id {id_aluno} deletado pelo usuario {usuario_atual}.')

            return jsonify(AlunoService.delete(id_aluno))
        except AssertionError as error:
            logging.error(f'Erro ao deletar aluno por ID: {error}')

            return str(error), 400

@alunos.route("/api/aluno/listAll", methods=['GET'])
@jwt_required()
def list_all():
    logging.info('Rota /api/aluno/listAll acessada.')

    return AlunoRepository.list_all()

@alunos.route("/api/aluno/findByRa", methods=['GET'])
@jwt_required()
def find_by_ra():
    logging.info('Rota /api/aluno/findByRa acessada.')

    ra = request.args.get('ra')
    try:
        return AlunoService.get_by_ra(ra)
    except AssertionError as error:
        logging.error(f'Erro ao buscar aluno aluno por ra: {error}')

        return str(error), 400
    
@alunos.route("/api/aluno/AusentesPresentes", methods=['GET'])
@jwt_required()
def ausentes_presentes():
    logging.info('Rota /api/aluno/AusentesPresentes acessada.')

    turma_id = request.args.get('id_turma')
    try:
        return AlunoService.ausentes_presentes(turma_id)
    except AssertionError as error:
        logging.error(f'Erro ao obter alunos ausentes e presentes: {error}')

        return str(error), 400
    
@alunos.route("/api/aluno/AtivoInativo", methods=['GET'])
@jwt_required()
def ativo_inativo():
    logging.info('Rota /api/aluno/AtivoInativo acessada.')

    turma_id = request.args.get('id_turma')
    try:
        return AlunoService.ativo_inativo(turma_id)
    except AssertionError as error:
        logging.error(f'Erro ao obter alunos ativos e inativos: {error}')

        return str(error), 400
    
@alunos.route("/api/aluno/mediaAtivo", methods=['GET'])
@jwt_required()
def media_ativo():
    logging.info('Rota /api/aluno/mediaAtivo acessada.')

    turma_id = request.args.get('id_turma')
    try:
        return AlunoService.media_ativo(turma_id)
    except AssertionError as error:
        logging.error(f'Erro ao obter media de alunos ativos: {error}')

        return str(error), 400
    
@alunos.route("/api/aluno/mediaAusente", methods=['GET'])
@jwt_required()
def media_ausente():
    logging.info('Rota /api/aluno/mediaAusente acessada.')

    turma_id = request.args.get('id_turma')
    
    try:
        return AlunoService.media_ausente(turma_id)
    except AssertionError as error:
        logging.error(f'Erro ao obter media de alunos ausentes: {error}')

        return str(error), 400

@alunos.route("/api/aluno/HistoricoPresenca", methods=['GET'])
@jwt_required()
def historico_presenca():
    logging.info('Rota /api/aluno/HistoricoPresenca acessada.')

    id_aluno = request.args.get('id_aluno')
    try:
        return AlunoService.historico_presenca(id_aluno)
    except AssertionError as error:
        logging.error(f'Erro ao obter historico de presencas de aluno por ID: {error}')

        return str(error), 400

@alunos.route("/api/aluno/PresencaFalta", methods=['GET'])
@jwt_required()
def presenca_falta():
    logging.info('Rota /api/aluno/PresencaFalta acessada.')

    id_aluno = request.args.get('id_aluno')
    try:
        return AlunoService.presenca_falta(id_aluno)
    except AssertionError as error:
        logging.error(f'Erro ao obter presencas e faltas de um aluno: {error}')

        return str(error), 400
    
@alunos.route("/api/aluno/ausentes", methods=['GET'])
@jwt_required()
def alunos_ausentes():
    logging.info('Rota /api/aluno/ausentes acessada.')

    try:
        return AlunoRepository.alunos_ausentes()
    except AssertionError as error:
        logging.error(f'Erro ao obter alunos ausentes: {error}')

        return str(error), 400
    
@alunos.route("/api/aluno/presentes", methods=['GET'])
@jwt_required()
def alunos_presentes():
    logging.info('Rota /api/aluno/presentes acessada.')

    try:
        return AlunoRepository.alunos_presentes()
    except AssertionError as error:
        logging.error(f'Erro ao obter alunos presentes: {error}')

        return str(error), 400
    
@alunos.route("/api/aluno/chegar", methods=['GET'])
@jwt_required()
def alunos_a_chegar():
    logging.info('Rota /api/aluno/chegar acessada.')

    try:
        return AlunoRepository.alunos_a_chegar()
    except AssertionError as error:
        logging.error(f'Erro ao obter alunos que faltam a chegar: {error}')

        return str(error), 400
    
@alunos.route("/api/aluno/alunoStatus", methods=['GET'])
@jwt_required()
def aluno_status():
    logging.info('Rota /api/aluno/alunoStatus acessada.')

    id_aluno = request.args.get('id_aluno')
    try:
        return AlunoService.aluno_status(id_aluno)
    except AssertionError as error:
        logging.error(f'Erro ao obter status de aluno por ID: {error}')

        return str(error), 400
    
@alunos.route("/api/aluno/turmaPresenca", methods=['GET'])
@jwt_required()
def alunos_presenca_turma():
    logging.info('Rota /api/aluno/turmaPresenca acessada.')

    turma_id = request.args.get('turma_id')
    try:
        return AlunoRepository.alunos_presenca_turma(turma_id)
    except AssertionError as error:
        logging.error(f'Erro ao obter presencas e falta de uma turma: {error}')

        return str(error), 400