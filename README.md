Após fazer o clone do projeto

Instalar os Requisitos - python, uvicorn, fastApi

Para rodar localmente:
    Uvicorn main:app --reload


/docs - Swagger UI

Get - /gabarito: Lista o gabarito de todas as provas cadastradas no sistema
Post - /gabarito: Cadastra uma nova prova e todo o seu gabarito assim -
como o peso das questões

Get - /Alunos: Lista os alunos cadastrados sistema com dados de prova -
e o gabarito dos mesmos.
Post - /Alunos: Cadastra um novo aluno e todo o seu gabarito com um maximo -
de 100 cadastros.
Post - /Alunos/inserir-prova/{cadastro-aluno}: inseri um novo gabarito -
a um aluno existente pelo seu numero de cadastro.

Post - /notas/{id}: View que retorna situação final do aluno 