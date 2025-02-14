import hashlib
from database import salvar_usuario, listar_usuarios

def hash_senha(senha):
    """Cria um hash seguro da senha usando SHA256."""
    return hashlib.sha256(senha.encode()).hexdigest()

def registrar_usuario(nome, email, username, senha):
    """Registra um novo usuário com senha hash."""
    senha_hash = hash_senha(senha)
    return salvar_usuario(nome, email, username, senha_hash)

def autenticar_usuario(username, senha):
    """Verifica se o usuário e senha são válidos."""
    senha_hash = hash_senha(senha)
    usuarios = listar_usuarios()
    for user in usuarios:
        if user["username"] == username and user["senha"] == senha_hash:
            return user
    return None
