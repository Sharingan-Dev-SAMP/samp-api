from http import HTTPStatus
from flask import Flask, jsonify, request
from samp_client.client import SampClient

app = Flask(__name__)

def handler(request):
    ip = request.args.get('ip')
    port = int(request.args.get('port', 7777))
    try:
        with SampClient(address=ip, port=port) as client:
            info = client.get_server_info()
            return jsonify({
                'online': True,
                'players': info.players,
                'max_players': info.max_players,
                'hostname': info.hostname,
                'gamemode': info.gamemode,
                'language': info.language
            })
    except Exception as e:
        return jsonify({'online': False, 'error': str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
