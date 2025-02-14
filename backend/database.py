import sqlite3
import json

DB_NAME = "database.db"
JSON_FILE = "usuarios.json"

def criar_tabela():
    """Cria a tabela de usuários no banco de dados SQLite se não existir."""
    conexao = sqlite3.connect(DB_NAME)
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            username TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL
        )
    ''')
    conexao.commit()
    conexao.close()

def salvar_usuario(nome, email, username, senha):
    """Salva um novo usuário no banco de dados e no JSON."""
    conexao = sqlite3.connect(DB_NAME)
    cursor = conexao.cursor()
    try:
        cursor.execute("INSERT INTO usuarios (nome, email, username, senha) VALUES (?, ?, ?, ?)",
                       (nome, email, username, senha))
        conexao.commit()
    except sqlite3.IntegrityError:
        return False
    finally:
        conexao.close()
    
    salvar_em_json()
    return True

def salvar_em_json():
    """Exporta os usuários do banco de dados para um arquivo JSON."""
    conexao = sqlite3.connect(DB_NAME)
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome, email, username FROM usuarios")
    usuarios = cursor.fetchall()
    conexao.close()

    lista_usuarios = [{"id": u[0], "nome": u[1], "email": u[2], "username": u[3]} for u in usuarios]
    
    with open(JSON_FILE, "w") as f:
        json.dump(lista_usuarios, f, indent=4)

def listar_usuarios():
    """Retorna todos os usuários cadastrados no banco de dados."""
    conexao = sqlite3.connect(DB_NAME)
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome, email, username FROM usuarios")
    usuarios = cursor.fetchall()
    conexao.close()
    return [{"id": u[0], "nome": u[1], "email": u[2], "username": u[3]} for u in usuarios]

criar_tabela()
