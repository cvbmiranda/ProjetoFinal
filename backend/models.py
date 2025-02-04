class Usuario:
    def __init__(self, nome, email, usuario, senha):
        self.nome = nome
        self.email = email
        self.usuario = usuario
        self.senha = senha

    def to_dict(self):
        """Converte os dados do usuário para um dicionário (útil para JSON)."""
        return {
            "nome": self.nome,
            "email": self.email,
            "usuario": self.usuario
        }
