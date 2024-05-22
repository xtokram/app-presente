from flask import Blueprint, request, jsonify
import logging
from flask_jwt_extended import jwt_required

from service.UsuarioService import UsuarioService

usuarios = Blueprint("usuario", __name__)

@usuarios.route("/api/usuario", methods=['GET', 'POST', 'PUT', 'DELETE'])
#@jwt_required()
def usuario():
    logging.info('Rota /api/usuario acessada.')
    if request.method == 'GET':
        id_usuario = request.args.get('id')
        try:
            return jsonify(UsuarioService.get_usuario_by_id(id_usuario))
        except AssertionError as error:
            logging.error(f'Erro ao obter usuário por ID: {error}')
            return str(error), 400
        
    if request.method == 'POST':
        data = request.json
                
        status = True
        login = data.get('login', 'NOT_FOUND')
        senha = data.get('senha', 'NOT_FOUND')
        nome = data.get('nome', 'NOT_FOUND')
        ra = data.get('ra', 'NOT_FOUND')
        cargo = data.get('cargo', 'NOT_FOUND')

        try:
            logging.info('Usuario registrado.')

            return UsuarioService.register(status=status, login=login, senha=senha, nome=nome, ra=ra, cargo=cargo)
        except AssertionError as error:
            logging.error(f'Erro ao registrar usuário: {error}')
            return str(error), 400
        
    if request.method == 'PUT':
        id_usuario = request.args.get('id')
        data = request.json

        status = True
        login = data.get('login', 'NOT_FOUND')
        senha = data.get('senha', 'NOT_FOUND')
        nome = data.get('nome', 'NOT_FOUND')
        ra = data.get('ra', 'NOT_FOUND')
        cargo = data.get('cargo', 'NOT_FOUND')

        try:
            logging.info('Usuario editado.')

            return UsuarioService.update(id_usuario=id_usuario, status=status, login=login, senha=senha, nome=nome, ra=ra, cargo=cargo)
        except AssertionError as error:
            logging.error(f'Erro ao editar usuário por ID: {error}')
            return str(error), 400

    if request.method == 'DELETE':
        id_usuario = request.args.get('id')
        try:
            logging.info('Usuario deletado.')

            return jsonify(UsuarioService.delete(id_usuario))
        except AssertionError as error:
            logging.error(f'Erro ao deletar usuário por ID: {error}')
            return str(error), 400
        
@usuarios.route("/api/login", methods=['POST'])
def login():
    if request.method == 'POST':

        data = request.json

        login = data.get('login', 'NOT_FOUND')
        senha = data.get('senha', 'NOT_FOUND')

        try:
            return UsuarioService.login(login=login, senha=senha)
             
        except AssertionError as error:
            logging.error(f'Erro na tentativa de realizar login: {error}')
            return str(error),400

