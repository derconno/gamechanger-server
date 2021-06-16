from time import time


class MongoConnector:

    def __init__(self):
        import pymongo
        self.mc = pymongo.MongoClient("mongodb://REDACTED")
        self.db = self.mc.get_database("REDACTED")

    def add_new_game(self, gameid, type, lastUpdate):
        self.db.get_collection("games").insert_one({
            "_id": gameid,
            "gametype": type,
            "lastUpdate": lastUpdate
        })

    def set_last_update(self, gameid, lastUpdate):
        self.db.get_collection("games").update_one(
            {"_id": gameid},
            {
                "$set": {
                    "lastUpdate": lastUpdate
                }
            }
        )

    def get_game(self, gameid):
        game = self.db.get_collection("games").find_one({"_id": gameid})
        if game is not None:
            game.pop("_id")
            return game

    def add_gamedata(self, gameid, points, calls, allowUpdates):
        self.db.get_collection("gamedata").insert_one({
            "_id": gameid,
            "Points": points,
            "Calls": calls,
            "allowUpdates": allowUpdates
        })
        self.set_last_update(gameid, int(time()))

    def update_gamedata(self, gameid, points, calls, allowUpdates):
        self.db.get_collection("gamedata").update_one(
            {"_id": gameid},
            {
                "$set": {
                    "Points": points,
                    "Calls": calls,
                    "allowUpdates": allowUpdates
                }
            }
        )
        self.set_last_update(gameid, int(time()))

    def get_gamedata(self, gameid):
        game = self.db.get_collection("gamedata").find_one({"_id": gameid})
        if game is not None:
            game.pop("_id")
            return game

    def get_all_gameids(self):
        return self.db.get_collection("games").distinct("_id")
