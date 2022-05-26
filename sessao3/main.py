from typing import Optional, Union
from fastapi import (
    FastAPI,
    HTTPException,
    status,
    Response,
    Path,
    Query,
    Header,
)
from fastapi.responses import JSONResponse
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


@app.get("/cursos/{curso_id}")
async def get_curso(
    curso_id: int = Path(
        default=None,
        title="ID do curso",
        description="Deve ser entre 1 e 4",
        gt=0,
        lt=5,
    )
):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Curso não Encontrado",
        )


@app.post("/cursos", status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso):
    next_id: int = len(cursos) + 1
    cursos[next_id] = curso
    del curso.id
    return curso


@app.put("/cursos/{curso_id}")
async def put_curso(curso_id: int, curso: Curso):
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id
        return curso
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Id do curso não encontrado",
        )


@app.delete("/cursos/{curso_id}")
async def delete_curso(curso_id: int):
    if curso_id in cursos:
        del cursos[curso_id]
        # return cursos
        # return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Id do curso não encontrado",
        )


@app.get("/calculadora")
async def calcular(
    a: int = Query(default=None, gt=5),
    b: int = Query(default=None, gt=10),
    x_header: Union[str, None] = Header(default=None),
    c: Optional[int] = None,
):
    soma = a + b
    if c:
        soma = soma + c

    print(f"Header: {x_header}")

    return {"resultado": soma}


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
