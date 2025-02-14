import asyncio
import websockets

conexoes = set()

async def handle_connection(websocket, path):
    conexoes.add(websocket)
    try:
        async for mensagem in websocket:
            for conn in conexoes:
                if conn != websocket:
                    await conn.send(mensagem)
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        conexoes.remove(websocket)

start_server = websockets.serve(handle_connection, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
