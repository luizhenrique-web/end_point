from fastapi import HTTPException

from repositories.usuario_repository import UsuarioRepository
from core.seguranca import gerar_hash, verificar_hash
from core.jwt import criar_token
from models.usuario import Usuario

class UsuarioService:
    def __init__(self, repository: UsuarioRepository):
        self.usuario_repository = repository
        
    def criar_usuario(self, dados):
        usuario_existente = self.usuario_repository.get_by_email(dados.email)
        if usuario_existente:
            raise HTTPException(status_code=400, detail="Email já cadastrado")
        
        senha_hash = gerar_hash(dados.senha)
        
        usuario = Usuario(
            nome=dados.nome,
            email=dados.email,
            senha=senha_hash
        )
        
        usuario= self.usuario_repository.create(usuario)
        return {
            "Mensagem": "Usuário criado com sucesso",
            "Objeto": {
                "id": usuario.id,
                "nome": usuario.nome,  
                "email": usuario.email
                }
        }
        
    def listar_usuarios(self):
        usuarios = self.usuario_repository.get_all()
        
        return{
            "Mensagem": "Usuários encontrados",
            "Total": len(usuarios),
            "Objetos": usuarios
        }
        
    def buscar_usuarios(self, usuario_id: int):
        usuario = self.usuario_repository.get_by_id(usuario_id)
        
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        
        return {
            "Mensagem": "Usuário encontrado",
            "Objeto": usuario
        }
        
    def autenticar_usuario(self, email: str, senha: str):

        usuario = self.usuario_repository.get_by_email(email)

        if not usuario:
            raise HTTPException(
                status_code=401,
                detail="Credenciais inválidas",
            )

        senha_valida = verificar_hash(senha, usuario.senha)

        if not senha_valida:
            raise HTTPException(
                status_code=401,
                detail="Credenciais inválidas",
            )

        token = criar_token(
            {
                "sub": str(usuario.id),
                "email": usuario.email,
            }
        )

        return {"access_token": token, "token_type": "bearer"}
