from fastapi import Response, APIRouter, Cookie

roteador = APIRouter()

@roteador.get("/tema/{tema}")
def definir_tema(tema: str, response: Response):
    response.set_cookie(
        key="tema", 
        value=tema, 
        max_age=3600
    ) 
    
    return {
        "Mensagem": "Tema definido com sucesso",
        "Tema": tema,
    }
    
@roteador.get("/tema")
def obter_tema(tema: str = Cookie(default="claro")):
    return {"Tema": tema}