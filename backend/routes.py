from flask import Blueprint, request, jsonify
from auth import registrar_usuario, autenticar_usuario
from database import listar_usuarios

routes = Blueprint("routes", __name__)

@routes.route("/register", methods=["POST"])
def register():
    data = request.json
    if not all(k in data for k in ("nome", "email", "username", "senha")):
        return jsonify({"error": "Dados incompletos"}), 400

    if registrar_usuario(data["nome"], data["email"], data["username"], data["senha"]):
        return jsonify({"message": "Usuário registrado com sucesso"}), 201
    return jsonify({"error": "Usuário já existe"}), 409

@routes.route("/login", methods=["POST"])
def login():
    data = request.json
    user = autenticar_usuario(data["username"], data["senha"])
    if user:
        return jsonify({"message": "Login bem-sucedido", "user": user}), 200
    return jsonify({"error": "Usuário ou senha incorretos"}), 401

@routes.route("/users", methods=["GET"])
def users():
    return jsonify(listar_usuarios()), 200
