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
        tournament_list.append(Player.deserialize(t))
        print(tournament_list)


def load_player():
    load_db = TinyDB("player_db.json")
    load_table = load_db.table("players")
    for p in load_table:
        players_list.append(Player.deserialize(p))

        
"""def back_up_tournament():
    back_up_db_p = TinyDB("backup_player.json")
    back_up_table_p = back_up_db_p.table("player_db_backup")
    back_up_db_tour = TinyDB("back_up_tour.json")
    back_up_table_tour = back_up_db_tour.table("tournaments")
    for b in back_up_table_p:
        back_up_players.append(Player.deserialize(b))
    for t in back_up_table_tour:
        back_up_tournament.append(Tournament.deserialize(t))
    for save_t in tournament_list:
        print(save_t.serialize())
    for save_p in players_list:
        print(save_p.serialize())"""
        
def current_tournament_load():
    controler = HomeController()
    controler.display_main_page()

#load_player()
#load_tournament()

#print(tournament_load(tournament_list))
current_tournament_load()
