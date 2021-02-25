import json
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    data = None
    with open('/home/pi/Documents/hsys/humidity-control/current.txt', 'r') as f:
        data = json.loads(f.read())
    return render_template('index.html', temp=data['t'], humidity=data['h'], time=data['time'])
