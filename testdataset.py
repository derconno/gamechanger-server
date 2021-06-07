import random

# TODO we need more data!

games = {
    420: {"gametype": "Rommee"},
    710: {"gametype": "Wizard"},
    1337: {"gametype": "Wizard"}
}

gamedata = {
    420: {
        "Points": {
            "Julian": [8, 40, 56, 50, 64],
            "Niklas": [0, 10, 14, 32, 49],
            "Conno": [13, 23, 42, 42, 69],
            "Paula": [12, 12, 12, 76, 76]
        },
        "allowUpdates": False,
        "Calls": {}
    },
    710: {
        "Points": {
            "Janne":  [20, 40, 20, 10, 50, 120, 140, 200, 110, 10],
            "Niklas": [-10, 10, 40, 30, 20, 10, 80, 60, 120, 110],
            "Conno":  [-10, 10, 40, 80, 60, 80, 70, 150, 60, 140],
            "Paula":  [-10, 10, 40, 30, 80, 70, 60, 50, -40, 60]
        },
        "Calls": {
            "Janne":  [1, 1, 1, 2, 2, 3, 1, 3, 0, 0],
            "Niklas": [1, 1, 0, 1, 2, 3, 0, 3, 3, 3],
            "Conno":  [1, 0, 0, 2, 2, 1, 3, 0, 0, 4],
            "Paula":  [1, 0, 0, 1, 0, 1, 3, 3, 0, 0]
        },
        "allowUpdates": False
    },
    1337: {
        "Points": {
            "Janne": [10, 30, 20, 60, 110, 50, 110, 90, 80, -20],
            "Niklas": [20, 40, 70, 150, 100, 140, 130, 120, 200, 180],
            "Conno": [10, 30, 20, 10, 50, -10, 30, 10, -80, -180],
            "Paula": [10, 30, 50, 90, 110, 50, 130, 210, 250, 350]
        },
        "Calls": {
            "Janne":  [0, 0, 1, 0, 0, 0, 3, 3, 2, 0],
            "Niklas": [1, 0, 0, 4, 0, 2, 3, 4, 4, 0],
            "Conno":  [0, 1, 2, 1, 2, 0, 2, 3, 0, 0],
            "Paula":  [0, 1, 1, 0, 1, 0, 0, 0, 2, 0]
        },
        "allowUpdates": False
    }
}


def get_id_for_gametype(gametype):
    if gametype == "Wizard":
        if random.randint(0, 1):
            return 710
        else:
            return 1337
    elif gametype == "Rommee":
        return 420
