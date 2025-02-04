import asyncio
import websockets
import json
from database import Database

class ServidorWebSocket:
    def __init__(self):
        self.clientes = set()
        self.db = Database()

    async def handler(self, websocket, path):
        self.clientes.add(websocket)
        try:
            async for mensagem in websocket:
                dados = json.loads(mensagem)

                if dados["tipo"] == "login":
                    sucesso = self.db.verificar_usuario(dados["usuario"], dados["senha"])
                    resposta = {"tipo": "login_resposta", "sucesso": sucesso}
                    await websocket.send(json.dumps(resposta))

                elif dados["tipo"] == "registro":
                    sucesso = self.db.inserir_usuario(dados["nome"], dados["email"], dados["usuario"], dados["senha"])
                    resposta = {"tipo": "registro_resposta", "sucesso": sucesso}
                    await websocket.send(json.dumps(resposta))  # Envia resposta imediatamente

        finally:
            self.clientes.remove(websocket)

    def iniciar(self):
        loop = asyncio.get_event_loop()
        servidor = websockets.serve(self.handler, "localhost", 8765)
        loop.run_until_complete(servidor)
        loop.run_forever()

if __name__ == "__main__":
    ServidorWebSocket().iniciar()
