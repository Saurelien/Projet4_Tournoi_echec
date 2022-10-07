from tournoi.controlers import HomeController
from tournoi.models import Player, Tournament, players_list, tournament_list
from tinydb import TinyDB

"""créer une méthode pour load les joueurs et aussi pour les tournois load tournament"""
"""Si le tournoi est en cours " True " mettre en sauvegarde les données entrées par l'utilisateur dans un db json nommé current_t.json pour chaque étape validé de l'utilisateur
Pour se faire créer une methode dans la classe tournament qui va verifier la validation des données inscrite dans la sauvegarde current_t.json"""

def load_tournament():
    
    load_db = TinyDB("db.json")
    load_table = load_db.table("tournaments")
    for t in load_table:
        print(t)
        tournament_list.append(Tournament.deserialize(t))
    for load_tournament_data in tournament_list:
        print(load_tournament_data.serialize())

def load_player():
    load_db = TinyDB("player_db.json")
    load_table = load_db.table("players")
    for p in load_table:
        players_list.append(Player.deserialize(p))
    for load in players_list:
        print(load.serialize())

def current_tournament_load():
    pass


load_player()
load_tournament()
#print(tournament_load(tournament_list))

controler = HomeController()
controler.display_main_page()
