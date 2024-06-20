from flask import Blueprint, request, jsonify
import logging
from repository.TurmaRepository import TurmaRepository

from service.TurmaService import TurmaService

from flask_jwt_extended import jwt_required, get_jwt_identify

turmas = Blueprint("turmas", __name__)

@turmas.route("/api/turma", methods=['GET', 'POST', 'PUT', 'DELETE'])
@jwt_required()
def turma():
    usuario_atual = get_jwt_identify().get('nome')
    logging.info(f'Rota /api/turma acessada pelo usuario {usuario_atual}.')
    if request.method == 'GET':
        id_turma = request.args.get('id')
        try:
            return jsonify(TurmaService.get_turma(id_turma))
        except AssertionError as error:
            logging.error(f'Erro ao obter turma por ID: {error}')
            return str(error), 400 

    if request.method == 'POST':
        data = request.json
        
        status = True
        id_materia = data.get('id_materia', 'NOT_FOUND')
        nome = data.get('nome', 'NOT_FOUND')
        ano = data.get('ano', 'NOT_FOUND')
        semestre = data.get('semestre', 'NOT_FOUND')
        turno = data.get('turno', 'NOT_FOUND')
        modalidade = data.get('modalidade', 'NOT_FOUND')
        curso = data.get('curso', 'NOT_FOUND')

        try:
            logging.info(f'Turma registrada pelo usuario {usuario_atual}.')

            return TurmaService.post_turma(status, id_materia, nome, ano, semestre, turno, modalidade, curso)
        except AssertionError as error:
            logging.error(f'Erro ao cadastrar turma: {error}')
            return str(error), 400

    if request.method == 'PUT':
        id_turma = request.args.get('id')
        data = request.json

        status = True
        id_materia = data.get('id_materia', 'NOT_FOUND')
        nome = data.get('nome', 'NOT_FOUND')
        ano = data.get('ano', 'NOT_FOUND')
        semestre = data.get('semestre', 'NOT_FOUND')
        turno = data.get('turno', 'NOT_FOUND')
        modalidade = data.get('modalidade', 'NOT_FOUND')
        curso = data.get('curso', 'NOT_FOUND')

        try:
            logging.info(f'Turma editada pelo usuario {usuario_atual}.')

            return TurmaService.update(id_turma=id_turma, id_materia=id_materia, status=status, nome=nome, ano=ano, semestre=semestre, turno=turno, modalidade=modalidade, curso=curso)
        except AssertionError as error:
            logging.error(f'Erro ao editar turma por ID: {error}')
            return str(error), 400

    if request.method == 'DELETE':
        id_turma = request.args.get('id')

        try:
            logging.info(f'Turma deletada pelo usuario {usuario_atual}.')

            return jsonify(TurmaService.delete(id_turma))
        except AssertionError as error:
            logging.error(f'Erro ao deletar turma por ID: {error}')
            return str(error), 400

@turmas.route("/api/turma/listAll", methods=['GET'])
@jwt_required()
def listar_all_turmas():
    logging.info('Rota /api/turma/listAll acessada.')
    return TurmaRepository.list_all()

@turmas.route("/api/turma/cadastrarAluno", methods=['POST'])
@jwt_required()
def cadastrar_aluno():
    usuario_atual = get_jwt_identify().nome
    logging.info('Rota /api/turma/cadastrarAluno acessada.')
    data = request.json

    id_turma = data['id_turma']
    id_aluno = data['id_aluno']

    try:
        logging.info(f'Aluno {id_aluno} registrado na turma {id_turma} pelo usuario {usuario_atual}')
        return TurmaService.cadastrar_aluno(id_turma, id_aluno)
    except AssertionError as error:
        logging.error(f'Erro ao cadastrar aluno na turma: {error}')
        return str(error), 400

@turmas.route("/api/turma/cadastrarProfessor", methods=['POST'])
@jwt_required()
def cadastrar_professor():
    logging.info('Rota /api/turma/cadastrarProfessor acessada.')
    data = request.json

    id_turma = data['id_turma']
    id_professor = data['id_professor']

    try:
        return TurmaService.cadastrar_professor(id_turma, id_professor)
    except AssertionError as error:
        logging.error(f'Erro ao cadastrar professor na turma: {error}')
        return str(error), 400