import json

def listar_usuarios_json():
    arquivo_json = "usuarios.json"
    try:
        with open(arquivo_json, "r", encoding="utf-8") as f:
            usuarios = json.load(f)
            print("\n📋 Lista de Usuários Registrados:\n")
            for idx, user in enumerate(usuarios, start=1):
                print(f"{idx}. Nome: {user['nome']} | Email: {user['email']} | Usuário: {user['usuario']}")
    except FileNotFoundError:
        print("❌ Nenhum usuário registrado ainda.")
    except json.JSONDecodeError:
        print("❌ Erro ao ler o arquivo JSON.")

if __name__ == "__main__":
    listar_usuarios_json()
