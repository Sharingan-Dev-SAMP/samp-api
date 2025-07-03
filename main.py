from fastapi import FastAPI, HTTPException
from samp_client.client import SampClient

app = FastAPI()

@app.get("/check/{ip_port}")
async def check_server(ip_port: str):
    try:
        ip, port = ip_port.split(":")
        port = int(port)
        
        with SampClient(address=ip, port=port) as client:
            info = client.get_server_info()
            clients = client.get_server_clients()[:5]
            players = [{"name": client.name, "ping": client.ping} for client in clients]
            
            return {
                "online": True,
                "players": info.players,
                "max_players": info.max_players,
                "hostname": info.hostname,
                "gamemode": info.gamemode,
                "language": info.language,
                "passworded": "Yes" if info.password else "No",
                "active_players": players
            }
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid IP:port format. Use ip:port (e.g., 51.254.178.238:7777)")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
