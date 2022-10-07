from tournoi.controlers import HomeController
from tournoi.models import Player, Tournament, players_list, tournament_list
from tinydb import TinyDB

"""créer une méthode pour load les joueurs et aussi pour les tournois load tournament"""
tournament_list = list()

def tournament_load():
    
    load_db = TinyDB("db.json")
    load_table = load_db.table("tournaments")
    for t in load_table:
        print(t)
        tournament_list.append(Tournament.deserialize(t))

def load_player():
    load_db = TinyDB("player_db.json")
    load_table = load_db.table("players")
    for p in load_table:
        print(p)
        players_list.append(Player.deserialize(p))


def current_tournament_load():
    pass

tournament_load()
load_player()
#print(tournament_load(tournament_list))

controler = HomeController()
controler.display_main_page()
