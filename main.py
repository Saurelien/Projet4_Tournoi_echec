from tournoi.controlers import HomeController
from tournoi.models import Player, Tournament, tournament_list, players_list
from tinydb import TinyDB

"""créer une méthode pour load les joueurs et aussi pour les tournois load tournament"""

players_list.append(Player.player_finalized(Player))
tournament_list.append(Tournament.tournament_finalized(Tournament))
print(players_list.append(Player.player_finalized(Player)))

"""tour = list()
player_in_list = list()"""

db = TinyDB("tournament_db.json")
tournament_table = db.table("turnaments")
for tournament in tournament_table:
    tournament_list.append(Tournament.deserialize_tournament(tournament))
for t in tournament_list:
    print(t.tournament_serialized(t))
controler = HomeController()
controler.display_main_page()
