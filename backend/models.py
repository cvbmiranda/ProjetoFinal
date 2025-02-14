class Usuario:
    def __init__(self, nome, email, username, senha):
        self.nome = nome
        self.email = email
        self.username = username
        self.senha = senha  # A senha será armazenada já com hash

    def to_dict(self):
        """Retorna um dicionário representando o usuário (sem a senha)."""
        return {
            "nome": self.nome,
            "email": self.email,
            "username": self.username
        }
