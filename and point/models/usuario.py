from sqlalchemy import Column, Integer, String

from core.database import Base

class Usuario(Base):
    
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    nome = Column(String(200), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    senha = Column(String(255), nullable=False)