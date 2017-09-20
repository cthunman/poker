mongod --fork --logpath data/logs/mongod.log --dbpath data/db
export FLASK_APP=server.py
flask run

