from pydantic import BaseModel, EmailStr

# Request 
class EstudanteCreate(BaseModel):
    nome: str
    email: EmailStr
    idade: int

# Response
class EstudanteResponse(BaseModel):
    id: int
    nome: str
    email: EmailStr
    idade: int
    
class Config:
    from_attributes = True