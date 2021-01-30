import json
import os

from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
card_data_file = os.path.join(basedir, 'static/AllPrintings.json')

# A welcome message to test our server
@app.route('/')
def index():
    return render_template('indexProduction.html')

def card_internal(card_json):
    return {
        'name': card_json['name'],
        'rarity': card_json['rarity'],
        'scryfallId': card_json['identifiers']['scryfallId'],
        'gathererId': card_json['identifiers'].get('multiverseId', ''),
        'text': card_json.get('text', '')
    }

def get_all_cards(set=None):
    with open(card_data_file, 'r', encoding='utf8') as jsonfile:
        file_data = json.loads(jsonfile.read())
    card_data = file_data['data']
    if set:
        try:
            return card_data[set]['cards']
        except KeyError:
            return {'error': 'Could not find set symbol'}
    return card_data

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
    cards = get_all_cards(set)
    html = '<html><body style="width:100%"><style>.card {flex: 1} .card img {width:250px; height:350px} .card-container {display: flex; flex-wrap: wrap;}</style>'
    html += '<div class="card-container">'
    for c_json in cards:
        card = card_internal(c_json)
        html += '<div class="card"><img src="https://api.scryfall.com/cards/{}?format=image"></img></div>'.format(card['scryfallId'])
    html += '</div></body></html>'
    return html
