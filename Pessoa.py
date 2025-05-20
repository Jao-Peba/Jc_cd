from datetime import datetime 

class Data:

    def __init__(self, data):
        dia, mes, ano = list(map(int, data.split("/")))
        self.data = datetime(ano,mes,dia)
    
    

class Pessoa():
    def __init__(
        self,
        id: int,
        nome: str,
        data_nascimento: Data,
        profissao: str,
        escolaridade: str,
        estado_civil: str,
        sexo: str
    ):
        self.id = id
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.profissao = profissao
        self.escolardade = escolaridade
        self.estado_civil = estado_civil
        self.sexo = sexo
        self.idade = self.calcular_idade()

    def calcular_idade(self):

        hoje = datetime.now()
        data_nascimento = Data(self.data_nascimento).data

        idade = hoje.year - data_nascimento.year
        
        if (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day):
            idade -= 1

        return idade