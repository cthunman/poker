from flask import Flask
from pymongo import MongoClient

from jinja2 import Environment, PackageLoader, select_autoescape
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
    print(opponent_hands)
    template = env.get_template('collection.html')
    return template.render(opponent_hands=opponent_hands)
