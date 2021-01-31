import json

from .cards import *

from flask import Flask, request, jsonify, render_template
app = Flask(__name__)
app.debug = True


# A welcome message to test our server
@app.route('/')
def index():
    return render_template('indexProduction.html')

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
