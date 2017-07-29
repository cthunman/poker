from pymongo import MongoClient
c = MongoClient()
db = c.test_database
collection = db.test_collection

post = {'cards': ['AS', 'KD']}
posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)
