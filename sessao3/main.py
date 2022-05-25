from fastapi import FastAPI

app = FastAPI()


cursos = {
    1:{"Titulo": "Programação para Leigos",
       "aulas": 112,
       "horas": 58, },
    2:{"Titulo": "Algorimo e Lógica de Programação",
       "aulas": 100,
       "horas": 60, },
    3:{"Titulo": "FastAPI - APIs Modernas e Assíncronas com Python",
       "aulas": 150,
       "horas": 80, },
    4:{"Titulo": "Banco de dados para Leigos",
       "aulas": 120,
       "horas": 90, },
}


@app.get("/cursos")
async def get_cursos():
    return cursos


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app", host="0.0.0.0", port=8000, log_level="info", reload=True
    )
