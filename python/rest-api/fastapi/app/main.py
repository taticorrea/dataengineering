from fastapi import FastAPI

app = FastAPI()

cursos = [
    {
        "id": 1,
        "nome": "Cálculo Diferencial e Integral I",
        "credito": 20,
        "professor": "Ivan"
    },
    {
        "id": 2,
        "nome": "Cálculo Diferencial e Integral II",
        "credito": 20,
        "professor": "Morelli"
    },
    {
        "id": 3,
        "nome": "Física da Matéria Condensada",
        "credito": 10,
        "professor": "José Leite"
    },
    {
        "id": 4,
        "nome": "Mecânica Geral",
        "credito": 20,
        "professor": "José Mahon"
    },
    {
        "id": 5,
        "nome": "Física Matemática I",
        "credito": 20,
        "professor": "Barci"
    }
]

alunos = [
    {
        "id": 1,
        "nome": "Tatiane",
        "cpf": "12345678910",
        "matricula": "0000000001",
        "idade": 12
    },
    {
        "id": 2,
        "nome": "Jessica",
        "cpf": "12345678911",
        "matricula": "0000000002",
        "idade": 11
    },
    {
        "id": 3,
        "nome": "Victor",
        "cpf": "12345678912",
        "matricula": "0000000003",
        "idade": 10
    },
    {
        "id": 4,
        "nome": "Lecy",
        "cpf": "12345678913",
        "matricula": "0000000004",
        "idade": 40
    },
    {
        "id": 5,
        "nome": "Elias",
        "cpf": "12345678914",
        "matricula": "0000000005",
        "idade": 44
    },
    {
        "id": 6,
        "nome": "Bryan",
        "cpf": "12345678915",
        "matricula": "0000000006",
        "idade": 5
    }
]

@app.get("/alunos")
def get_alunos():
    return alunos

@app.get("/cursos")
def get_cursos():
    return cursos    