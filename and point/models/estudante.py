from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from core.database import Base

class Estudante(Base):
    __tablename__ = "estudantes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(150), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    idade = Column(Integer, nullable=False)
    criado_em = Column(DateTime, server_default=func.now())