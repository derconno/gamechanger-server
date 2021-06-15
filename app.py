from time import time
from random import randint

from flask import Flask, request

import testdataset

app = Flask(__name__)


@app.route("/game/<int:gameid>", methods = ["GET"])
def get_game(gameid):
    data = testdataset.games[gameid]
    return data

@app.route("/game/<int:gameid>/data", methods = ["GET"])
def get_game_data(gameid):
    if not gameid in testdataset.gamedata.keys():
        return 'no such game', 404
    return testdataset.gamedata[gameid]

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
    while id in testdataset.games.keys():
        id = randint(0, 420)
    testdataset.games[id] = {"gametype": gametype, "lastUpdate": int(time())}

    points = {}
    calls = {}
    for p in players:
        points[p] = []
        calls[p] = []

    testdataset.gamedata[id] = {
        "Points": points,
        "Calls": calls,
        "allowUpdates": False
    }
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
    if not gameid in testdataset.gamedata.keys():
        return 'no such game', 404
    testdataset.games[gameid]["lastUpdate"] = int(time())
    testdataset.gamedata[gameid]["Points"] = points
    testdataset.gamedata[gameid]["Calls"] = calls
    return '', 200