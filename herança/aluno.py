
from pessoa import pessoa

class Aluno(pessoa):
    def __init__(self, nome, cpf, idade):
        super(Aluno, self).__init__()