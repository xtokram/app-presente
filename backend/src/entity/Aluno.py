from repository.MainRepository import MainRepository

class Aluno(MainRepository.db.Model):
    __tablename__ = 'alunos'
    idAluno = MainRepository.db.Column(MainRepository.db.Integer, primary_key=True)
    idUsuario = MainRepository.db.Column(MainRepository.db.Integer, MainRepository.db.ForeignKey('usuarios.id_usuario'))
    status = MainRepository.db.Column(MainRepository.db.Boolean, nullable=False)
    ausente = MainRepository.db.Column(MainRepository.db.Boolean, nullable=False)
    nome = MainRepository.db.Column(MainRepository.db.String(100), nullable=False)
    ra = MainRepository.db.Column(MainRepository.db.Integer, nullable=False, unique=True)
    usuario = MainRepository.db.relationship('Usuario', back_populates='aluno')
    presencas = MainRepository.db.relationship('Presenca', back_populates='aluno')
    turmas = MainRepository.db.relationship('Turma', secondary='turma_aluno')    

    def __init__(self, status:bool, ausente:bool, nome:str, ra:int):
        self.status = status
        self.ausente = ausente
        self.nome = nome
        self.ra = ra
        



