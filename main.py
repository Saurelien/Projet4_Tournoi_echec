from tournoi.controlers import HomeController
from tournoi.models import Player, Tournament, players_list, tournament_list
from tinydb import TinyDB, Query

"""créer une méthode pour load les joueurs et aussi pour les tournois load tournament"""
tournament_list = list()
data = Query()

"""def player_load(players):
    
    load_db = TinyDB("tournament_db.json")
    load_table = load_db.table("tournaments")
    for player in players_list:
        load_db.get(data.first_name)
        load_table.append(player.player_serialized(players))
    for p in load_table:
        players_list.append(Player.deserialize_player(p))
    return players_list"""


def tournament_load():
    
    load_db = TinyDB("db.json")
    load_table = load_db.table("tournaments")
    for t in load_table:
        print(t)
        tournament_list.append(Tournament.deserialize(t))
    print(tournament_list)

def load_player():
    load_db = TinyDB("player_db.json")
    load_table = load_db.table("players")
    for p in load_table:
        print(p)
        print(players_list.append(Player.deserialize(p)))


def current_tournament_load():
    pass

tournament_load()
load_player()
#print(tournament_load(tournament_list))

controler = HomeController()
controler.display_main_page()
