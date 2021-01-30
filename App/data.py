from typing import List, Dict, Union
from fastapi import HTTPException

Item = Dict[str, Dict[str, Union[int, Dict[str, int]]]]

student_interface = list[Dict[str, Union[list[str], str, int, float]]]
class GabaritoProva:
    gabarito: List[Item] = [
        {
            "prova": 0,
            "respostas": {"A": 3, "D": 3, "C": 2, "B": 1, "E": 1},
        },
        {

            "prova": 1,
            "respostas": {"B": 2, "D": 2, "C": 2, "A": 2, "E": 2}
        },
        {

            "prova": 2,
            "respostas": {"B": 2, "D": 2, "C": 2, "A": 2, "E": 2}
        }

    ]
    questao_atual = 0
    peso_atual = 0

    def listar(self):
        return self.gabarito

    def inserir_questao(self, item: Item) -> Item:
        self.questao_atual += 1
        item["questao"] = self.questao_atual
        self.gabarito.append(item)
        return item

class GabaritoAluno:
    cadastro_alunos: student_interface = [
        {
            "Cadastro_do_aluno": 1,
            "Nome_do_aluno": "Jhon Doe",
            "Resposta_do_aluno": [{"prova": 0, "respostas": ['d', 'a', 'C']}],
            "Nota_final": 3.0
        }

    ]

    def __init__(self):
        self._cadastro = 1

    def listar_aluno(self):
        return self.cadastro_alunos


    def inserir_prova_no_aluno(self, id, prova):
        self.cadastro_alunos[id]['Resposta_do_aluno'].append(prova)

        return prova


    def inserir_cadastro(self, item: Item) -> (Item, str):
        self._cadastro += 1
        item["Cadastro_do_aluno"] = self._cadastro
        if len(self.cadastro_alunos) > 99:
            raise HTTPException(status_code=409, detail="Numero de alunos excedeu a capacidade permitida")
        self.cadastro_alunos.append(item)
        return item


provas = GabaritoProva()

alunos = GabaritoAluno()


def pega_as_provas_do_aluno(id_do_aluno):
    return alunos.cadastro_alunos[id_do_aluno]['Resposta_do_aluno']


def pegar_gabarito_da_prova(id_prova):
    for prova in provas.gabarito:

        if prova['prova'] != id_prova:
            return prova["respostas"]


def calcula_nota_da_prova(gabarito, prova):
    current_nota = 0
    for i in gabarito:
        for j in prova:
            if i.upper() == j.upper():
                current_nota += int(gabarito[i])
    return current_nota