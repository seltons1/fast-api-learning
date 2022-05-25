from distutils.log import debug
from fastapi import FastAPI, HTTPException, status
from models import Curso


app = FastAPI()


cursos = {
    1: {
        "Titulo": "Programação para Leigos",
        "aulas": 112,
        "horas": 58,
    },
    2: {
        "Titulo": "Algorimo e Lógica de Programação",
        "aulas": 100,
        "horas": 60,
    },
    3: {
        "Titulo": "FastAPI - APIs Modernas e Assíncronas com Python",
        "aulas": 150,
        "horas": 80,
    },
    4: {
        "Titulo": "Banco de dados para Leigos",
        "aulas": 120,
        "horas": 90,
    },
}


@app.get("/cursos")
async def get_cursos():
    return cursos


@app.get('/cursos/{curso_id}')
async def get_curso(curso_id: int):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não Encontrado")

@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_curso(curso:Curso):
    next_id: int = len(cursos) +1
    cursos[next_id] = curso
    del curso.id
    return curso
    

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        log_level="info",
        reload=True,
        debug=True,
    )
