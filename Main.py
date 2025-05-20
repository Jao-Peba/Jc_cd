import json
from fastapi import FastAPI
from Objeto import Objeto
from Pessoa import Pessoa
from PessoaModel import PessoaModelo
from PessoaModel import ObjetoModelo

p1 = Pessoa(
    '1',
    'JoãoPeba',
    '11/12/1998',
    'Proplayer de Valorant',
    'Gamer',
    'Solteiro',
    'Masculino',
    )

p2 = Pessoa(
    '2',
    'Laricela',
    '20/10/2006',
    'Cientista de Dados Sênior',
    'Superior',
    'Muito que bem',
    'Feminino'
    )

p3 = Pessoa(
    '3',
    'Matheus',
    '12/05/1999',
    'VideoMaker',
    'Superior',
    'Casado',
    'Masculino'
    )

p4 =  Pessoa(
    '4',
    'César',
    '31/12/2003',
    'Motorista de aplicativo',
    'Superior',
    'Casado',
    'Masculino'
    )


lista_pessoas = [
        p1,p2,p3,p4
    ]

ob1 = Objeto(
    '1',
    'Placa-mãe',
    'Setor_eletronica',
    'Esgotado'
    )
ob2 = Objeto(
    '2',
    'Teclado',
    'Setor_periféricos',
    'Em estoque'
    )

ob3 = Objeto(
    '3',
    'Gopro',
    'setor_periféricos',
    'Esgotado'
    
)
ob4 = Objeto(
    '4',
    'Celular',
    'setor_eletronica',
    'Em estoque'
)
lista_objetos = [
        ob1,ob2,ob3,ob4
    ]


app = FastAPI()#Variável classe FastAPI

#@ = Anotation, função que tem como parâmetro a função abaixo dela.
@app.get('/')
def minha_api():
    return 'Bem-vindo a minha API, para Usuários, acesse a rota /api/users ou então para objetos /api/produtos'

@app.get('/api/users')
def users_api():
    return(lista_pessoas)

@app.get('/api/v2/users')
def read_api(nome: str = ''):
    with open('user.json') as arquivos:
        users = json.loads(arquivos.read())
        
    if nome:
        filtered_users = []

        for user in users:
            if user['nome'].startswitch(nome):
                filtered_users.append(user)        
        return filtered_users
    
    return users
    
    
@app.get('/api/users/{id_pessoa}')
def get_pessoa(id_pessoa):
    for pessoa in lista_pessoas:
        if pessoa.id == id_pessoa:
            return pessoa
        
    return lista_pessoas[1]

@app.get('/api/v2/users/{id_pessoa}')
def get_pessoa(id_pessoa):
    with open('user.json') as arquivos:
        pessoas = json.loads(arquivos.read())
    
    for pessoa in pessoas:
        if pessoa.id == id_pessoa:
            return pessoa
        
    return "Pessoa não encontrada"

@app.get('/api/users/{nome_pessoa}')
def get_pessoa(nome_pessoa: str):
    for pessoa in lista_pessoas:
        if pessoa.nome == nome_pessoa:
            return pessoa
        
    return lista_pessoas[1]

@app.post('/api/v3/users/')
def post_pessoa(pessoa: PessoaModelo):
    with open('user.json', encoding='utf-8') as arquivo:
        pessoas = list(json.loads(arquivo.read()))
    
    pessoa.id = pessoas[-1]['id'] + 1
    pessoas.append(pessoa.model_dump())
    
    with open('user.json', 'w', encoding='utf-8') as arquivo:
        arquivo.write(json.dumps(pessoas, indent=4))

    return f'Pessoa com nome {pessoa.nome} criada com sucesso'

@app.delete('/api/v3/users/{id}')
def delete_pessoa(id: int):
    with open('user.json', encoding='utf-8') as arquivo:
        pessoas = list(json.loads(arquivo.read()))

    for posicao in range(len(pessoas)):
        print(posicao)
        if pessoas[posicao]['id'] == id:
            pessoas.pop(posicao)

            with open('user.json', 'w', encoding='utf-8') as arquivo:
                arquivo.write(json.dumps(pessoas, indent=4))

            return 'pessoa foi de vala'

    return 'pessoa nao existe'

@app.patch ('/api/v3/users/{id}')
def update_pesoas(id: int):
    with open('user.json', encoding='utf-8') as arquivo:
        pessoas = list(json.loads(arquivo.read()))

@app.get('/api/produtos')
def produtos_api():
    return(lista_objetos)

@app.get('/api/v2/produtos')
def read_api(nome_obj: str = ''):
    with open('objeto.json') as arquivos:
        objetos = json.loads(arquivos.read())
    
    if nome_obj:
        filtered_objetos =[]
    
        for objeto in objetos:
            if objeto['nome_obj'].startswitch(nome_obj):
                filtered_objetos.append(objeto)
            return filtered_objetos
    return objetos

@app.post('/api/v3/produtos/')
def post_objeto(objeto: ObjetoModelo):
    with open('objeto.json', encoding='utf-8') as arquivo:
        objetos = list(json.loads(arquivo.read()))

    objeto.id = objetos[-1]['id_obj']+1
    objetos.append(objeto.model_dump())

    with open('objeto.json', 'w', encoding='utf-8') as arquvio:
        arquivo.write(json.dumps(objetos, indent=4))
    return f'Objeto {objeto.nome_obj} colocado no estoque com sucesso'

@app.delete('/api/v3/produtos/{id_obj}')
def delete_objeto(id_obj:int):
    with open('objeto.json', encoding='utf-8') as arquivo:
        objetos = list(json.loads(arquivo.read()))
    
    for posicao in range(len(objetos)):
        print(posicao)
        if objetos[posicao]['id_obj'] == id_obj:
            pessoas.pop(posicao)
        
            with open('objeto.json', 'w', encontrada='utf-8') as arquivo:
                arquivo.write(json.dumps(pessoas,indent=4))

            return 'objeto saiu do estoque'

    return 'objeto nao existe'

@app.patch('/api/v3/produtos/{id_obj}')
def update_objetos(id_obj: int):
    with open('user.json', encoding='utf-8') as arquivo:
        pessoas = list(json.loads(arquivo.read()))

    