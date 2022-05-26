from typing import Optional
from pydantic import BaseModel


class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: str
    horas: int


cursos = [
    Curso(id=1, titulo="Programação para Leigos", aulas=112, horas=58),
    Curso(
        id=2, titulo="Algorimo e Lógica de Programação", aulas=100, horas=90
    ),
    Curso(
        id=3,
        titulo="FastAPI - APIs Modernas e Assíncronas com Python",
        aulas=150,
        horas=100,
    ),
    Curso(id=4, titulo="Banco de dados para Leigos", aulas=120, horas=90),
]
