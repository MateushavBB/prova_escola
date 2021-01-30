from fastapi import FastAPI, HTTPException
from App.data import GabaritoProva, GabaritoAluno, pega_as_provas_do_aluno, pegar_gabarito_da_prova, calcula_nota_da_prova
from App.modelos import ModeloDoGabarito, RespostaDosAlunos, Prova

app = FastAPI()
gabarito = GabaritoProva()
cadastro_alunos = GabaritoAluno()


@app.get("/gabarito", tags=["Prova"])
def listar_gabarito():
    """
    view que retorna o gabarito da prova
    """
    return GabaritoProva.listar(gabarito)


@app.post("/gabarito", response_model=ModeloDoGabarito, status_code=201, tags=["Prova"])
def inserir_gabarito(item_a_inserir: ModeloDoGabarito):
    """
    Root view, insere na lista de itens a fazer
    """
    return gabarito.inserir_questao(item_a_inserir.dict())


@app.get("/Alunos", tags=["Alunos"])
def listar_cadastros():
    """
    view que retorna os alunos e suas respostas
    """
    return cadastro_alunos.listar_aluno()

@app.post("/Alunos", response_model=RespostaDosAlunos, status_code=201, tags=["Alunos"])
def inserir_cadastro(item_a_inserir: RespostaDosAlunos):
    """
    Root view, insere cadastro dos alunos
    """
    return cadastro_alunos.inserir_cadastro(item_a_inserir.dict())

@app.post("/Alunos/inserir-Prova/{cadastro-Aluno}", response_model=Prova, status_code=201, tags=["Alunos"])
def inserir_prova_no_aluno(codigo_aluno, nova_prova: Prova):
    """
    Root view, insere provas aos alunos
    """
    return cadastro_alunos.inserir_prova_no_aluno(int(codigo_aluno), nova_prova)

@app.get('/notas/{id}', status_code=200, tags=["Notas"])
def pegar_nota_do_aluno(id_do_aluno):
    """
    Root view, insere provas aos alunos
    """
    if len(cadastro_alunos.cadastro_alunos) <= int(id_do_aluno):
        raise HTTPException(status_code=409, detail="codigo/id do aluno inexistente")
    provas_do_aluno = pega_as_provas_do_aluno(int(id_do_aluno))
    lista_de_notas = []
    for provas in provas_do_aluno:
        for prova in provas:
            gabarito_atual = pegar_gabarito_da_prova(prova)
            # print(gabarito_atual)
            # print(provas[prova])
            if gabarito_atual is not None:
                lista_de_notas.append(calcula_nota_da_prova(gabarito_atual, provas[prova]))
    return lista_de_notas
