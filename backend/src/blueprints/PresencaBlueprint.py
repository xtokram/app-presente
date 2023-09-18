from flask import Blueprint, request, jsonify

from repository.MainRepository import MainRepository
from repository.PresencaRepository import PresencaRepository

from entity.Presenca import Presenca

from service.PresencaService import PresencaService

presencas = Blueprint("presencas", __name__)

@presencas.route("/api/presenca", methods=['GET', 'POST', 'PUT', 'DELETE'])
def presencasMain():
    if request.method == 'GET':
        id = request.args.get('id')
        try:
            return jsonify(PresencaService.getById(id))
        except AssertionError as error:
            return str(error)
    
    if request.method == 'POST':
        data = request.json

        idAluno = data['idAluno']
        idChamada = data['idChamada']
        status = True
        tipo_presenca = data['tipoPresenca']
        horario = data['horario']

        try:
            return PresencaService.register(idAluno, idChamada, status, tipo_presenca, horario)
        except AssertionError as error:
            return str(error)
    
    if request.method == 'PUT':
        id = request.args.get('id')
        data = request.json

        return PresencaService.update(id,data)
    
    if request.method == 'DELETE':
        id = request.args.get('id')
        return PresencaService.delete(id)

@presencas.route("/api/presenca/listAll", methods=['GET'])
def listAll():
    return PresencaRepository.listAll()

@presencas.route("/api/presenca/findByPresentes", methods=['GET'])
def findByPresentes():
    return PresencaRepository.findByPresentes()