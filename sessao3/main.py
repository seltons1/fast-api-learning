from typing import Any, Dict, Optional, Union, List
from fastapi import (
    FastAPI,
    HTTPException,
    status,
    Response,
    Path,
    Query,
    Header,
    Depends,
)

# from fastapi.responses import JSONResponse
from time import sleep
from models import Curso, cursos


def fake_db():
    try:
        print("abrindo conexão db ")
        sleep(5)
    finally:
        print("fechando conexão")
        sleep(2)


app = FastAPI(
    title="API de Cursos",
    version="0.2.1",
    description="API para aprender a utilização do FastAPI",
)


@app.get(
    "/cursos",
    description="Retorna todos os cursos armazenados no banco de dados",
    summary="Retorna todos os cursos",
    response_model=List[Curso],
    response_description="Cursos Encontrados",
)
async def get_cursos(db: Any = Depends(fake_db)):
    return cursos


@app.get(
    "/cursos/{curso_id}",
    description="Retorna o curso armazenados no banco de dados com o ID passado",
    summary="Retorna o curso com o ID passado",
)
async def get_curso(
    curso_id: int = Path(
        default=None,
        title="ID do curso",
        description="Deve ser entre 1 e 4",
        gt=0,
        lt=5,
    ),
    db: Any = Depends(fake_db),
):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Curso não Encontrado",
        )


@app.post(
    "/cursos",
    status_code=status.HTTP_201_CREATED,
    description="Cadastra um novo curso no banco de dados",
    summary="Cadastrar um novo curso",
    response_model=Curso,
)
async def post_curso(curso: Curso, db: Any = Depends(fake_db)):
    next_id: int = len(cursos) + 1
    cursos[next_id] = curso
    del curso.id
    return curso


@app.put(
    "/cursos/{curso_id}",
    description="Atualiza um curso armazenado no banco de dados com o ID passado",
    summary="Atualiza um curso com o ID passado",
)
async def put_curso(curso_id: int, curso: Curso, db: Any = Depends(fake_db)):
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id
        return curso
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Id do curso não encontrado",
        )


@app.delete(
    "/cursos/{curso_id}",
    description="Deleta o curso armazenado no banco de dados pelo ID",
    summary="Deleta um curso pelo ID",
)
async def delete_curso(curso_id: int, db: Any = Depends(fake_db)):
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


@app.get(
    "/calculadora",
    description="Utilização de Query parameters e Header",
    summary="Query parameters e Header",
)
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
