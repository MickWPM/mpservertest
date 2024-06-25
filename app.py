from flask import Flask, request, jsonify
import threading
import time
import os

app = Flask(__name__)

player_positions = {}
running = True

def game_simulation():
    while running:
        time.sleep(1)
        print("Game state updated")

@app.route('/move', methods=['POST'])
def move_player():
    player_id = request.json['player_id']
    direction = request.json['direction']
    
    if player_id not in player_positions:
        player_positions[player_id] = {'x': 0, 'y': 0}
    
    if direction == 'up':
        player_positions[player_id]['y'] += 1
    elif direction == 'down':
        player_positions[player_id]['y'] -= 1
    elif direction == 'left':
        player_positions[player_id]['x'] -= 1
    elif direction == 'right':
        player_positions[player_id]['x'] += 1
    
    print(f"Player {player_id} moved {direction}")
    return jsonify({"status": "Move successful"}), 200

@app.route('/state', methods=['GET'])
def get_game_state():
    print("State requested")
    return jsonify(player_positions), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

simulation_thread = threading.Thread(target=game_simulation)
simulation_thread.start()