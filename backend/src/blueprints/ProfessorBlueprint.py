from flask import Blueprint, request, jsonify
import logging
from repository.ProfessorRepository import ProfessorRepository

from flask_jwt_extended import jwt_required, get_jwt_identity

from service.ProfessorService import ProfessorService

professores = Blueprint("professores", __name__)

@professores.route("/api/professor", methods=['GET', 'POST', 'PUT', 'DELETE'])
@jwt_required()
def professor():
    usuario_atual = get_jwt_identity()

    logging.info(f'Rota /api/professor acessada pelo usuario {usuario_atual}.')
    if request.method == 'GET':
        id_professor = request.args.get('id')
        try:
           return jsonify(ProfessorService.get_by_id(id_professor))
        except AssertionError as error:
            logging.error(f'Erro ao obter professor por ID: {error}')
            return str(error), 400

    if request.method == 'POST':
        data = request.json

        status = True
        id_usuario = data.get('id_usuario', 'NOT_FOUND')
        nome = data.get('nome', 'NOT_FOUND')

        try:
            logging.info(f'Professor {nome} registrado pelo usuario {usuario_atual}.')

            return ProfessorService.register(id_usuario=id_usuario, status=status, nome=nome)
        except AssertionError as error:
            logging.error(f'Erro ao registrar professor por ID: {error}')
            return str(error), 400  


    if request.method == 'PUT':
        id_professor = request.args.get('id')
        data = request.json

        status = True
        nome = data.get('nome', 'NOT_FOUND')
        try:
            logging.info(f'Professor com id {id_professor} editado pelo usuario {usuario_atual}.')

            return ProfessorService.update(id_professor=id_professor, status=status, nome=nome)
        except AssertionError as error:
            logging.error(f'Erro ao editar professor por ID: {error}')
            return str(error), 400
        
    if request.method == 'DELETE':
        id_professor = request.args.get("id")
        try:
            logging.info(f'Professor com id {id_professor} deletado pelo usuario {usuario_atual}.')

            return jsonify(ProfessorService.delete(id_professor))
        except AssertionError as error:
            logging.error(f'Erro ao deletar professor por ID: {error}')
            return str(error), 400



@professores.route("/api/professor/listAll", methods=['GET'])
@jwt_required()
def listar_all_professores():
    logging.info('Rota /api/professorlistAll acessada.')
    return ProfessorRepository.list_all()

@professores.route("/api/professor/listarTurmas", methods=['GET'])
@jwt_required()
def listar_turmas():
    logging.info('Rota /api/professor/listarTurmas acessada.')
    id_professor = request.args.get("id")
    try:
        return ProfessorService.listar_turmas(id_professor)
    except AssertionError as error:
        logging.error(f'Erro ao listar turmas: {error}')
        return str(error), 400
    
@professores.route("/api/professor/numAlunos", methods=['GET'])
@jwt_required()
def num_alunos():
    logging.info('Rota /api/professor/numAlunos acessada.')
    id_professor = request.args.get("id_professor")
    id_chamada = request.args.get("id_chamada")
    
    try:
        return ProfessorService.num_alunos(id_professor, id_chamada)
    except AssertionError as error:
        logging.error(f'Erro ao tentar verificar numero de alunos: {error}')
        return str(error), 400
    
@professores.route("/api/professor/historicoSemanal", methods=['GET'])
@jwt_required()
def historico_semanal():
    logging.info('Rota /api/professor/historicoSemanal acessada.')
    id_turma = request.args.get("id")
    try:
        return ProfessorService.historico_semanal(id_turma)
    except AssertionError as error:
        logging.error(f'Erro ao tentar verificar historico semanal: {error}')
        return str(error), 400
    
@professores.route("/api/professor/mediaSemanal", methods=['GET'])
@jwt_required()
def media_semanal():
    logging.info('Rota /api/professor/mediaSemanal acessada.')
    id_turma = request.args.get("id")
    try:
        return ProfessorService.media_semanal(id_turma)
    except AssertionError as error:
        logging.error(f'Erro ao tentar verificar media de alunos por semana: {error}')
        return str(error), 400
