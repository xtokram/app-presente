from flask import Blueprint, request, jsonify

from repository.MateriaRepository import MateriaRepository
from flask_jwt_extended import jwt_required
from service.MateriaService import MateriaService

from utils import oidc

materias = Blueprint("Materia", __name__)   

@materias.route("/api/materia", methods=['GET', 'POST','PUT','DELETE'])
#@jwt_required()
@oidc.accept_token()
def materia():
    if request.method == 'GET':
        id_materia = request.args.get('id')
        try:    
            return jsonify(MateriaService.get_by_id(id_materia))
        except AssertionError as error:
            return str(error), 400
    
    if request.method == 'POST':
        data = request.json
    
        status = True
        nome = data.get('nome', 'NOT_FOUND')

        try:
            return MateriaService.register(status=status, nome=nome)
        except AssertionError as error:
            return str(error), 400
    
    if request.method == 'PUT':
        id_materia = request.args.get('id')
        data = request.json

        status = True
        nome = data.get('nome', 'NOT_FOUND')

        try: 
            return MateriaService.update(id_materia=id_materia, status=status, nome=nome)
        except AssertionError as error:
            return str(error), 400
    
    if request.method == 'DELETE':
        id_materia = request.args.get('id')
        try:
            return jsonify(MateriaService.delete(id_materia))
        except AssertionError as error:
            return str(error), 400
    
@materias.route("/api/materia/listAll", methods=['GET'])
@jwt_required()
def listar_all_materias():
    return MateriaRepository.list_all()