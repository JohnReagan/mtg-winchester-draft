import json

from .cards import *

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__, static_folder='../build', static_url_path='/')
app.debug = True
# TODO  configure key and CORS correctly
# set up CORS to allow react dev server to request
CORS(app)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins='*')


# A welcome message to test our server
@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/cards')
def cards():
    set = request.args.get('set')
    if not set:
        return json.dumps({'error': 'No set provided'})
    cards = get_all_cards(set)
    cards_final = [card_internal(c_json) for c_json in cards]
    return json.dumps(cards_final)

@app.route('/cards-visual')
def cards_visual():
    set = request.args.get('set')
    if not set:
        return json.dumps({'error': 'No set provided'})
    cards = get_booster(set)
    html = '<html><body style="width:100%"><style>.card {flex: 1} .card img {width:250px; height:350px} .card-container {display: flex; flex-wrap: wrap;}</style>'
    html += '<div class="card-container">'
    for card in cards:
        html += '<div class="card"><img src="https://api.scryfall.com/cards/{}?format=image"></img></div>'.format(card.scryfallId)
    html += '</div></body></html>'
    return html

@socketio.on('my event')
def test_message(message):
    emit('my response', {'data': message['data']})

@socketio.on('my broadcast event')
def test_broadcast(message):
    emit('my response', {'data': message['data']}, broadcast=True)

@socketio.on('connect')
def test_connect():
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')