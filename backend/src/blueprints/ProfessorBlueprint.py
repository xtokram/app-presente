from flask import Blueprint, request, jsonify

from repository.ProfessorRepository import ProfessorRepository
from repository.MainRepository import MainRepository

from entity.Professor import Professor

from service.ProfessorService import ProfessorService

professores = Blueprint("professores", __name__)

@professores.route("/api/professor", methods=['GET', 'POST', 'PUT', 'DELETE'])
def professor():
    if request.method == 'GET':
        id = request.args.get('id')
        try:
           return jsonify(ProfessorService.getProfessor(id))
        except AssertionError as error:
            return str(error)

    if request.method == 'POST':
        data = request.json

        idProfessor = data['idProfessor']
        idUsuario = data['idUsuario']
        ativo = data['ativo']
        nome = data['nome']

        try:
            return ProfessorService.register(idProfessor, idUsuario, ativo, nome)
        except AssertionError as error:
            return str(error)        


    if request.method == 'PUT':
        id = request.args.get('id')
        data = request.json

        idProfessor = data['idProfessor']
        idUsuario = data['idUsuario']
        ativo = data['ativo']
        nome = data['nome']

        try:
            return jsonify(ProfessorService.update(id, idProfessor, idUsuario, ativo, nome))
        except AssertionError as error:
            return str(error)
        
    if request.method == 'DELETE':
        id = request.args.get("id")
        try:
            return jsonify(ProfessorRepository.delete(id))
        except AssertionError as error:
            return str(error)



@professores.route("/api/professor/listAll", methods=['GET'])
def listarAllProfessores():
   return ProfessorRepository.listAll()