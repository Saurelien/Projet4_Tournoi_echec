from tournoi.controlers import HomeController
from tournoi.models import Player, Tournament
from tinydb import TinyDB, Query

"""créer une méthode pour load les joueurs et aussi pour les tournois load tournament"""
players_list = list()
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
    return players_list


def tournament_load(tournament):
    
    load_db = TinyDB("tournament_db.json")
    load_db.all()
    tournament_list.append(tournament)
    return tournament_list"""

def load_player(player_name):

    load_db = TinyDB("tournament_db.json")
    load_table = load_db.table("tournaments")
    """for player in players_list:
        load_table.insert(player.player_serialized())
    for p in load_table:
        players_list.append(Player.deserialize_player(int(p)))
    for player_p in players_list:
        print(player_p.player_serialized(player_name))"""
    player = load_db.contains(data.name)
    print(player)
    return player
    
        

def current_tournament_load():
    pass

print(load_player(players_list))
#print(tournament_load(tournament_list))

controler = HomeController()
controler.display_main_page()
