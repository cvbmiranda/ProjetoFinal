import asyncio
import websockets

conexoes = set()

async def handle_connection(websocket, path):
    conexoes.add(websocket)
    try:
        async for mensagem in websocket:
            for conn in conexoes:
                if conn != websocket:  # Evita enviar a mensagem de volta ao remetente
                    await conn.send(mensagem)
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        conexoes.remove(websocket)

async def main():
    async with websockets.serve(handle_connection, "localhost", 8765):
        print("Servidor WebSocket rodando em ws://localhost:8765")
        await asyncio.Future()  # Mantém o servidor rodando indefinidamente

if __name__ == "__main__":
    asyncio.run(main())  # Inicia corretamente o loop no Python 3.12+
