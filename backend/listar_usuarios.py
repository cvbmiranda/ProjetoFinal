from database import listar_usuarios

usuarios = listar_usuarios()
if usuarios:
    print("Usuários cadastrados:")
    for user in usuarios:
        print(f"ID: {user['id']} | Nome: {user['nome']} | Email: {user['email']} | Username: {user['username']}")
else:
    print("Nenhum usuário cadastrado ainda.")
