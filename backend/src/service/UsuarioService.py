from repository.UsuarioRepository import UsuarioRepository

from entity.Usuario import Usuario
from entity.CargoEnum import Cargo

from dtos.UsuarioDTO import UsuarioDTO



import re

class UsuarioService():
    @staticmethod
    def get_usuario_by_id(id):
        assert id != None, "Nenhum ID enviado."
        assert int(id) if isinstance(id, (int,str)) and id.isdigit() else None, "ID incorreto."
        assert int(id) > 0 and int(id) < 999999, "ID inválido."
        assert Usuario.query.get(id) != None, "Nenhum usuário com este ID foi encontrado."
    
        return UsuarioRepository.get_usuario_by_id(id)
    
    @staticmethod
    def register(status, login, senha, nome, ra, cargo):     

        assert login != 'NOT_FOUND', "Campo 'login' inexistente."
        assert cargo != 'NOT_FOUND', "Campo 'cargo' inexistente."
        assert senha != 'NOT_FOUND', "Campo 'senha' inexistente."
        assert nome != 'NOT_FOUND', "Campo 'nome' inexistente."
    

        cargos = [x.value for x in Cargo]
        assert cargo in cargos, "Cargo inválido"

        assert len(login) > 3, "login com tamanho inválido."
        assert login.isalpha(), "O username deve conter apenas letras."

        assert len(senha) > 6, "Tamanho de senha mínimo não atingido."
        assert not re.match(r'^[a-zA-Z]+$', senha), "senha deve conter números, letras maiúsculas e caractéres especiais."

        assert len(nome) > 2, "nome com tamanho inválido."

        

        assert not Usuario.query.filter(Usuario.login == login).first(), "Esse login já está sendo usado"
        
        if (cargo != "Aluno"):
                    ra = None
        else:
            assert ra != 'NOT_FOUND', "Campo 'ra' inexistente."
            assert not Usuario.query.filter(Usuario.ra == ra).first(), "RA já esta sendo usado."
            assert re.match(r'^\d+$', str(ra)), "O RA deve ter apenas números."
            assert ra >= 100000 and ra <= 999999, "RA inválido."

        usuario = UsuarioService.to_entity(UsuarioDTO(status=status, login=login, senha=senha, nome=nome, ra=ra, cargo=cargo))
        
        return UsuarioRepository.register(usuario)
    
    @staticmethod
    def update(id_usuario, status, login, senha, nome, ra, cargo):      

        assert login != 'NOT_FOUND', "Campo 'login' inexistente."
        assert cargo != 'NOT_FOUND', "Campo 'cargo' inexistente."
        assert senha != 'NOT_FOUND', "Campo 'senha' inexistente."
        assert nome != 'NOT_FOUND', "Campo 'nome' inexistente."
        assert ra != 'NOT_FOUND', "Campo 'ra' inexistente."

        assert len(login) > 3, "login com tamanho inválido."
        assert login.isalpha(), "O login deve conter apenas letras."

        assert len(senha) > 6, "Tamanho de senha mínimo não atingido."
        assert not re.match(r'^[a-zA-Z]+$', senha), "senha deve conter números, letras maiúsculas e caractéres especiais."
        
        assert len(nome) > 2, "nome com tamanho inválido."

        if (cargo != "Aluno"):
            ra = None

        usuario = UsuarioService.to_entity(UsuarioDTO(status=status, login=login, senha=senha, nome=nome, ra=ra, cargo=cargo))

        return UsuarioRepository.update(id_usuario, usuario) 

    @staticmethod
    def delete(id):
        
        assert int(id) if isinstance(id, (int,str)) and id.isdigit() else None, "ID incorreto."
        assert int(id) > 0 and int(id) < 999999, "ID inválido"
        assert Usuario.query.filter(Usuario.id_usuario == id).first() is not None, "Usuario não encontrado" 
        return UsuarioRepository.delete(id)      


    @staticmethod
    def to_entity(usuario_dto):
        usuario = Usuario(status=usuario_dto.status, login=usuario_dto.login, senha=usuario_dto.senha, nome=usuario_dto.nome, ra=usuario_dto.ra, cargo=usuario_dto.cargo)       
        
        return usuario
    
    @staticmethod
    def login(login, senha):
        assert login != 'NOT_FOUND', "Campo 'login' inexistente."
        assert senha != 'NOT_FOUND', "Campo 'senha' inexistente."
        
        assert len(login) > 3 and len(login) < 25, "Login inválido!!"

        assert login != None and len(login) > 0, "Insira um Login!"
        assert senha != None and len(senha) > 0, "Insira uma senha!"

        user = Usuario.query.filter(Usuario.login == login).first()
        # assert Usuario.query.filter(Usuario.login == login).first() is not None, "Login ou senha incorretos"
        assert user is not None, "Login ou senha incorretos"

        assert Usuario.verifyPassword(password=user.senha,given_password=senha), "Login ou senha incorretos!"

        return UsuarioRepository.login(login)


