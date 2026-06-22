from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer

from jose import jwt, JWTError

from core.jwt import CHAVE_SECRETA, ALGORITMO

schema_auth = OAuth2PasswordBearer(
    tokenUrl="/usuarios/login",
)

def obter_usuario_logado(
    token: str = Depends(schema_auth)
):
    try:
        payload = jwt.decode(
            token, 
            CHAVE_SECRETA, 
            algorithms=[ALGORITMO]
            )
        
        usuario_id: str = payload.get("sub")
        
        if not usuario_id:
            raise HTTPException(
                status_code=401,
                detail="Token inválido",
            )
        return payload
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Token inválido",
        )