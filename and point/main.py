from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.database import Base
from core.database import motor

from rotas.saude import roteador as saude_roteador
from rotas.estudantes import roteador as estudantes_roteador
from rotas.usuario import roteador as usuario_roteador

Base.metadata.create_all(bind=motor)

app = FastAPI(
    title="Mini API de Estudantes",
    description="Primeira API do curso de progamador web",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou ["http://127.0.0.1:5500"]
    allow_credentials=True,
    allow_methods=["*"], # GET, POST, PUT, PATCH, DELETE...
    allow_headers=["*"],
)

app.include_router(saude_roteador)
app.include_router(estudantes_roteador)
app.include_router(usuario_roteador)

@app.get("/")
def root():
    return {
        "application": "MiniAPI",
        "version": "1.0.0",
        "docs": "/docs",
        "saude": "/saude",
        "saude_banco": "/saude/db"
    }