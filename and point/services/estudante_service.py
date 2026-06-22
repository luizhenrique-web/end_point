from fastapi import HTTPException

from models.estudante import Estudante
from repositories.estudante_repository import EstudanteRepository

class EstudanteService:
    def __init__(self, repository: EstudanteRepository):
        self.repository = repository
        
    def criar_estudante(self, dados):
        estudante_existente = self.repository.get_by_email(dados.email)
        
        if estudante_existente:
            raise HTTPException(status_code=400, detail="Email já cadastrado")
        
        estudante = Estudante(
            nome=dados.name,
            email=dados.email,
            idade=dados.idade
        )
        return self.repository.create(estudante)
    
    def listar_estudantes(self):
        return self.repository.get_all()
    
    def buscar_estudante_por_id(self, estudante_id: int):
        estudante = self.repository.get_by_id(estudante_id)
        
        if not estudante:
            raise HTTPException(status_code=404, detail="Estudante não encontrado")
       
        return estudante
    
    def excluir_estudante(self, estudante_id: int):
        estudante = self.buscar_estudante(estudante_id)
        
        self.repository.delete(estudante)
        return estudante
        
       