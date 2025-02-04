import sqlite3
import json
import os

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("usuarios.db", check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            usuario TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL
        )
        """)
        self.conn.commit()

    def inserir_usuario(self, nome, email, usuario, senha):
        try:
            self.cursor.execute("INSERT INTO usuarios (nome, email, usuario, senha) VALUES (?, ?, ?, ?)", 
                                (nome, email, usuario, senha))
            self.conn.commit()

            # Adicionar usuário no arquivo JSON
            self.salvar_usuario_json(nome, email, usuario)

            return True
        except sqlite3.IntegrityError:
            return False  # Retorna falso se o usuário ou email já existirem

    def salvar_usuario_json(self, nome, email, usuario):
        arquivo_json = "usuarios.json"
        dados = []

        # Se o arquivo já existir, carregamos os dados existentes
        if os.path.exists(arquivo_json):
            with open(arquivo_json, "r", encoding="utf-8") as f:
                try:
                    dados = json.load(f)
                except json.JSONDecodeError:
                    dados = []

        # Adicionamos o novo usuário à lista
        dados.append({"nome": nome, "email": email, "usuario": usuario})

        # Salvamos no arquivo JSON
        with open(arquivo_json, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

    def listar_usuarios_json(self):
        arquivo_json = "usuarios.json"
        if os.path.exists(arquivo_json):
            with open(arquivo_json, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

