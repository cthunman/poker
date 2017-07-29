from pymongo import MongoClient
import pprint

c = MongoClient()
db = c.test_database
collection = db.test_collection

hands = [
    {'cards': ['AS', 'KD']},
    {'cards': ['QS', 'KD']},
    {'cards': ['AS', 'TD']},
    {'cards': ['2S', 'KD']},
    {'cards': ['7S', '8S']},
    {'cards': ['AS', 'AD']},
    {'cards': ['9D', 'JD']}
]
posts = db.posts
post_id = posts.insert_many(hands)
pprint.pprint(post_id)

# pprint.pprint(posts.find_one({'cards': ['AS', 'KD']}))
for p in posts.find({'cards': 'KD'}):
    pprint.pprint(p)
