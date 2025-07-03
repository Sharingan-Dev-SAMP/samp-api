import os
from flask import Flask, jsonify
from samp_client.client import SampClient

app = Flask(__name__)

@app.route('/check/<ip>/<int:port>')
def check_server(ip, port):
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
        return jsonify({'online': False, 'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
