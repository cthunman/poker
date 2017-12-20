from flask import Flask
from pymongo import MongoClient

from jinja2 import PackageLoader, Environment, select_autoescape
env = Environment(
    loader=PackageLoader('poker', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

app = Flask(__name__)
c = MongoClient()
db = c.plo


@app.route("/")
def index():
    template = env.get_template('collections.html')
    collections = db.collection_names()
    return template.render(collections=collections)


@app.route("/collection/<starting_hand>")
def collection(starting_hand):
    opponent_hands = db[starting_hand].distinct('opponent_hand')

    hand_stats = []
    for hand in opponent_hands:
        result = {'hand': hand}
        total = db[starting_hand].find({'opponent_hand': hand}).count()
        wins = db[starting_hand].find(
            {
                'opponent_hand': hand,
                'winning_players': [1]
            }).count()
        ties = db[starting_hand].find(
            {
                'opponent_hand': hand,
                'winning_players': [1, 2]
            }).count()
        losses = db[starting_hand].find(
            {
                'opponent_hand': hand,
                'winning_players': [2]
            }).count()
        result['win%'] = wins/total
        result['tie%'] = ties/total
        result['loss%'] = losses/total
        hand_stats.append(result)

    template = env.get_template('collection.html')
    context = {}
    context['opponent_hands'] = opponent_hands
    context['hand_stats'] = hand_stats
    context['starting_hand'] = starting_hand
    return template.render(context=context)
