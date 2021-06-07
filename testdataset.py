# TODO we need more data!

games = {
    420: {"gametype": "Rommee"},
    710: {"gametype": "Wizard"}
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
            "Julian": [8, 40, 56, 50, 64, 0, 0],
            "Niklas": [0, 10, 14, 32, 49, 0, 0],
            "Conno": [13, 23, 42, 42, 69, 0, 0],
            "Paula": [12, 12, 12, 76, 76, 0, 0]
        },
        "Calls": {
            "Julian": [1, 1, 3, 2, 4, 6, 4, 0],
            "Niklas": [1, 2, 3, 4, 5, 6, 7, 8],
            "Conno": [0, 1, 1, 2, 4, 5, 3, 8],
            "Paula": [2, 0, 0, 0, 0, 0, 0, 0]
        },
        "allowUpdates": False
    }
}

def get_id_for_gametype(gametype):
    if gametype == "Wizard":
        return 710
    elif gametype == "Rommee":
        return 420