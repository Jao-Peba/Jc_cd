from pydantic import BaseModel 

class PessoaModelo(BaseModel):
    id: int = None
    nome: str
class ObjetoModelo(BaseModel):
    id_obj: int = None
    nome_obj: str