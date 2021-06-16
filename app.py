from time import time
from random import randint

from flask import Flask, request

from .dbconnector import MongoConnector

app = Flask(__name__)

mc = MongoConnector()

@app.route("/game/<int:gameid>", methods = ["GET"])
def get_game(gameid):
    data = mc.get_game(gameid)
    if data is None:
        return 'no such game', 404
    return data

@app.route("/game/<int:gameid>/data", methods = ["GET"])
def get_game_data(gameid):
    data = mc.get_gamedata(gameid)
    if data is None:
        return 'no such game', 404
    return data

@app.route("/game", methods = ["PUT"])
def put_game():
    json_data = request.get_json()
    if not json_data:
        return 'no json data', 400
    gametype = json_data["gametype"]
    if not gametype:
        return 'wrong gametype', 400
    players = json_data["players"]
    if not players:
        return 'no players', 400
    id = randint(0, 420)
    while id in mc.get_all_gameids():
        id = randint(0, 420)
    mc.add_new_game(id, gametype, int(time()))

    points = {}
    calls = {}
    for p in players:
        points[p] = []
        calls[p] = []

    mc.add_gamedata(id, points, calls, False)
    return {"id": id}

@app.route("/game/<int:gameid>", methods = ["POST"])
def post_game(gameid):
    json_data = request.get_json()
    if not json_data:
        return 'no json data', 400
    points = json_data["Points"]
    if not points:
        return 'no Points', 400
    calls = json_data["Calls"]
    if not calls:
        calls = {}
    if mc.get_game(gameid) is None:
        return 'no such game', 404
    mc.update_gamedata(gameid, points, calls, False)
    return '', 200