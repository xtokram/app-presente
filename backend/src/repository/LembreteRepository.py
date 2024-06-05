from flask import jsonify
from models import db
from entity.CargoEnum import Cargo
from entity.Lembrete import Lembrete
from datetime import datetime

class LembreteRepository():
    @staticmethod
    def get_lembrete_by_id(id):
        try:
            return {
                "id_lembrete": Lembrete.query.get(id).id_lembrete,
                "id_secretaria" : Lembrete.query.get(id).id_secretaria,
                "destinatario_id": Lembrete.query.get(id).destinatario_id,
                "destinatario_cargo": Lembrete.query.get(id).destinatario_cargo.value,
                "titulo": Lembrete.query.get(id).titulo,
                "mensagem": Lembrete.query.get(id).mensagem,
                "criacao": Lembrete.query.get(id).criacao,
                "visualizacao": Lembrete.query.get(id).visualizacao,
                "status": Lembrete.query.get(id).status
            }
        except AttributeError as error:
            raise AssertionError ("Lembrete não existe.")
    @staticmethod
    def lista_all():
        lembretes = Lembrete.query.all()
        resultado = []
        for lembrete in lembretes:
            resultado.append({
                "id_lembrete" : lembrete.id_lembrete,
                "id_secretaria" : lembrete.id_secretaria, 
                "DestinatarioId": lembrete.destinatario_id,
                "destinatario_cargo": lembrete.destinatario_cargo.value,
                "Titulo": lembrete.titulo,
                "Mensagem": lembrete.mensagem,
                "Criacao": lembrete.criacao,
                "Visualizacao": lembrete.visualizacao,
                "status": lembrete.status
            })
        return jsonify(resultado)
    
    @staticmethod
    def update(id, lembrete):
        old_lembrete = Lembrete.query.get(id)
        
        old_lembrete.id_secretaria = lembrete.id_secretaria
        old_lembrete.destinatario_cargo = lembrete.destinatario_cargo
        old_lembrete.destinatario_id = lembrete.destinatario_id
        old_lembrete.titulo = lembrete.titulo
        old_lembrete.mensagem = lembrete.mensagem
        old_lembrete.criacao = lembrete.criacao
        old_lembrete.visualizacao = lembrete.visualizacao
        old_lembrete.status = lembrete.status

        db.session.merge(old_lembrete)
        db.session.commit()
        
        return f"Lembrete ID {id} atualizado."
    
    @staticmethod
    def delete(id):
        lembrete = Lembrete.query.get(id)
        
        lembrete.status = False

        db.session.merge(lembrete)
        db.session.commit()
        
        return f"Lembrete ID {id} deletado."
    
    @staticmethod
    def create(lembrete):
        db.session.add(lembrete)
        db.session.commit()
        
        return f"Lembrete ID {lembrete.id_lembrete} criado."

    @staticmethod
    def get_cargo(cargo:str, id:int):
        if cargo == "Aluno":
            texto = db.text(f"SELECT * FROM alunos WHERE id_aluno = {id}")

            with db.engine.connect() as connection:
                resultado = connection.execute(texto).fetchone()
                
                if resultado != None:
                    return resultado.id_aluno
                else:
                    raise AssertionError("Nenhum destinatario encontrado.")

        elif cargo == "Professor":
            texto = db.text(f"SELECT * FROM professores WHERE id_professor = {id}")

            with db.engine.connect() as connection:
                resultado = connection.execute(texto).fetchone()
                
                if resultado != None:
                    return resultado.id_professor
                else:
                    raise AssertionError("Nenhum destinatario encontrado.")
        elif cargo == "Secretaria":
            texto = db.text(f"SELECT * FROM secretarias WHERE id_secretaria = {id}")

            with db.engine.connect() as connection:
                resultado = connection.execute(texto).fetchone()
                
                if resultado != None:
                    return resultado.id_secretaria
                else:
                    raise AssertionError("Nenhum destinatario encontrado.")
        else:
            raise AssertionError("Cargo inválido.")
        
    @staticmethod
    def find_lembrete(cargo, id):

        lembretes = db.session.query(Lembrete).filter(Lembrete.destinatario_id == id).filter(Lembrete.destinatario_cargo == cargo).all()
        
        if lembretes:
            
            lembretes_data = []
            for lembrete in lembretes:
                lembrete_data = {
                'id':lembrete.id_secretaria,
                'Titulo': lembrete.titulo,
                'mensagem': lembrete.mensagem
                }
                lembretes_data.append(lembrete_data)
            

            return jsonify(lembretes_data)
        
        return jsonify([])
    
    @staticmethod
    def lembrete_visualizado(id_lembrete):

        lembrete = Lembrete.query.get(id_lembrete)

        lembrete.visualizacao = (datetime.now())

        db.session.merge(lembrete)
        db.session.commit()

        return f"Lembrete visualizado."
    
    @staticmethod
    def lembretes_visualizados():
        
        lembretes = db.session.query(Lembrete).filter(Lembrete.visualizacao != None).all()

        if lembretes:

            lembretes_data = []
            for lembrete in lembretes:
                lembrete_data = {
                    'id': lembrete.id_secretaria,
                    'Titulo': lembrete.titulo,
                    'mensagem': lembrete.mensagem
                }
                lembretes_data.append(lembrete_data)

            return jsonify(lembretes_data)
        
        return jsonify([])