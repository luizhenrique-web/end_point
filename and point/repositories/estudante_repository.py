from sqlalchemy.orm import Session

from models.estudante import Estudante


class EstudanteRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, estudante: Estudante):
        self.db.add(estudante)
        self.db.commit()
        self.db.refresh(estudante)
        return estudante
    
    def get_all(self):
        return self.db.query(Estudante).all()
    
    def get_by_id(self, estudante_id: int):
        return (
            self.db.query(Estudante)
            .filter(Estudante.id == estudante_id)
            .first()
            )
    
    def get_by_email(self, email: str):
        return (
            self.db.query(Estudante)
            .filter(Estudante.email == email)
            .first()
            )
        
    def delete(self, estudante: Estudante):
        self.db.delete(estudante)
        self.db.commit()