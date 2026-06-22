from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_banco 
from core.auth import obter_usuario_logado


from repositories.estudante_repository import EstudanteRepository
from services.estudante_service import EstudanteService
from schema.estudante_schema import EstudanteCreate, EstudanteResponse

roteador = APIRouter(
    prefix="/estudantes",
    tags=["Estudantes"]
)

@roteador.post(
    "", 
    response_model=EstudanteResponse,
    status_code=201
)
def criar(
    estudante: EstudanteCreate,
    db: Session = Depends(get_banco)
):
    repository = EstudanteRepository(db)
    service = EstudanteService(repository)
    return service.criar_estudante(estudante)

@roteador.get(
    "", 
    response_model=list[EstudanteResponse]
)
def listar(
    db: Session = Depends(get_banco)
):
    repository = EstudanteRepository(db)
    service = EstudanteService(repository)
    return service.listar_estudantes()

@roteador.get(
    "/{estudante_id}", 
    response_model=EstudanteResponse
)
def buscar(
    estudante_id: int,
    db: Session = Depends(get_banco)
):
    repository = EstudanteRepository(db)
    service = EstudanteService(repository)
    return service.buscar_estudante_por_id(estudante_id)

@roteador.delete(
    "/{estudante_id}", 
    response_model=EstudanteResponse
)
def excluir(
    estudante_id: int,
    db: Session = Depends(get_banco)
):
    repository = EstudanteRepository(db)
    service = EstudanteService(repository)
    return service.excluir_estudante(estudante_id)

#Rotas privadas - Necessário autenticação para acessar

@roteador.put("/estudantes/privada")
def rota_privada(
    db: Session = Depends(get_banco),
    usuario=Depends (obter_usuario_logado)
):
    return "Isso é uma rota privada, apenas usuários autenticados podem acessar"

@roteador.post("/estudantes/privada")
def rota_privada(
    db: Session = Depends(get_banco),
    usuario=Depends (obter_usuario_logado)
):
    return "Rota totalmente privada, apenas usuários autenticados podem acessar"

@roteador.delete("/estudantes/privada")
def rota_privada(
    db: Session = Depends(get_banco),
    usuario=Depends (obter_usuario_logado)
):
    return "Rota totalmente privada, apenas usuários autenticados podem acessar"