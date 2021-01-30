from pydantic import BaseModel
from typing import List, Dict, Union


class ModeloDoGabarito(BaseModel):
    prova: int
    resposta: List[Dict[str, Union[int, Dict[str, int]]]]


class RespostaDosAlunos(BaseModel):
    Nome_do_aluno: str
    Resposta_do_aluno: List[Dict[str, List[str]]]
    Nota_final: float

class Prova(BaseModel):
    prova: int
    respostas: List[str]
