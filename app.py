from time import time

from flask import Flask, request

import testdataset

app = Flask(__name__)


@app.route("/game/<int:gameid>", methods = ["GET"])
def get_game(gameid):
    data = testdataset.games[gameid]
    now = int(time())
    data["lastUpdate"] = now - (now % 30)
    return data

@app.route("/game/<int:gameid>/data", methods = ["GET"])
def get_game_data(gameid):
    return testdataset.gamedata[gameid]

@app.route("/game", methods = ["PUT"])
def put_game():
    json_data = request.get_json()
    if not json_data:
        return 'no json data', 400
    gametype = json_data["gametype"]
    if not gametype:
        return 'wrong gametype', 400
    if not json_data["players"]:
        return 'no players', 400
    id = testdataset.get_id_for_gametype(gametype)
    return {"id": id}

@app.route("/game/<int:gameid>", methods = ["POST"])
def post_game(gameid):
    json_data = request.get_json()
    if not json_data:
        return 'no json data', 400
    return '', 200