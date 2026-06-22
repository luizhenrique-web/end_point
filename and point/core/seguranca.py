from passlib.context import CryptContext

contexto_senha = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def gerar_hash(senha: str):
    return contexto_senha.hash(senha)

def verificar_hash(senha: str, hash_senha: str):
    return contexto_senha.verify(senha, hash_senha)

print(gerar_hash("luizito543boapessoa_2009")) 