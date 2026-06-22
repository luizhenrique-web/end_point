from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from core.database import get_banco

roteador= APIRouter(
    prefix="/saude",
    tags=["Saude Check"]
)

@roteador.get("")
def saude():
    return {
        "status": "UP",
        "servico":"estudante-api"
    }
    
@roteador.get("/db")
def saude_db(banco: Session = Depends(get_banco)):
    try:
        banco.execute(text("SELECT 1"))
        return {
            "status": "UP",
            "database":"conectado"
            
        }
    except Exception as error:
        return {
            "status": "DOWN",
            "database": "Desconectado",
            "ERRO": str(error)
        }