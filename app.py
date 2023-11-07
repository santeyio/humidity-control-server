import json
from flask import Flask, jsonify

CURRENT_READINGS_FILE_PATH = '/home/pi/Documents/hsys/humidity-control/current.txt'
#  CURRENT_READINGS_FILE_PATH = '/home/caleb/dev/humidity-control-server/sample_current.txt'

app = Flask(__name__, static_folder='static', static_url_path='/static')

@app.route('/readings')
def get_current_readings():
    data = None
    with open(CURRENT_READINGS_FILE_PATH, 'r') as f:
        data = json.loads(f.read())
    return jsonify({
        'temp': data['t'],
        'humidity': data['h'],
        'read_time': data['time'],
    })

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def hello_world(path):
    return app.send_static_file('index.html')
