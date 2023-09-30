from repository.PresencaRepository import PresencaRepository

from entity.Presenca import Presenca
from entity.Chamada import Chamada
from entity.Aluno import Aluno

class PresencaService():
    @staticmethod
    def get_by_id(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("Deve ser um número inteiro")
        
        assert int(id) > 0, "ID inválido."
        assert Presenca.query.get(id) != None, f"Nenhuma presença foi encontrada com o ID {id}"
        assert PresencaRepository.get_presenca_by_id(id)

    @staticmethod
    def register(presenca_dto):

        presenca = PresencaService.to_entity(presenca_dto)
        
        assert Chamada.query.filter(Chamada.status == True).first() is not None, "Não existe nenhuma chamada aberta"
        
         
        return PresencaRepository.register_presenca(Presenca(id_aluno=presenca.id_aluno, id_chamada=presenca.id_chamada, status=presenca.status, tipoPresenca=presenca.tipoPresenca, horario=presenca.horario))
    
    @staticmethod
    def update(id, presenca_dto):
        
        presenca = PresencaService.to_entity(presenca_dto)

        return PresencaRepository.update(id, presenca)
    
    @staticmethod
    def delete(id):
        try:
            int(id)
        except ValueError:
            raise AssertionError("Deve ser um número inteiro")
        
        return PresencaRepository.delete(id)
    
    @staticmethod
    def to_entity(aluno_dto):
        presenca = Presenca(id_aluno=aluno_dto.id_aluno, id_chamada=aluno_dto.id_chamada, status=aluno_dto.status, tipoPresenca=aluno_dto.tipoPresenca, horario=aluno_dto.horario)

        return presenca