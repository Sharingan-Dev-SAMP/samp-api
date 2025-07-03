from fastapi import FastAPI, HTTPException
from samp_client.client import SampClient

app = FastAPI()

@app.get("/check/{ip}/{port}")
async def check_server(ip: str, port: int):
    try:
        with SampClient(address=ip, port=port) as client:
            info = client.get_server_info()
            return {
                "online": True,
                "players": info.players,
                "max_players": info.max_players,
                "hostname": info.hostname,
                "gamemode": info.gamemode,
                "language": info.language
            }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
