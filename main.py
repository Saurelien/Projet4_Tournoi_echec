from tournoi.controlers import HomeController, ReportController
from tournoi.models import Player, Tournament, tournament_list, players_list
from tinydb import TinyDB



players_list.append(Player.player_finalized(Player))
tournament_list.append(Tournament.tournament_finalized(Tournament))

tour = list()
player_in_list = list()

"""player_db = TinyDB("player_db.json")
player_table = player_db.table("players")
tournament_db = TinyDB("tournament_db.json")
tournament_table = tournament_db.table("tournaments")"""
for tournament in tour:
    tour.append(Tournament.deserialize_tournament())
for t in tournament_list:
    print(Tournament.tournament_serialized(t))
"""for player_data in players_list:
    player_table.insert(Player.player_serialized(player_data))
for player in players_list:
    player_table.insert(player.player_serialized())
for tournament in tournament_list:
    tournament_table.insert(tournament.tournament_serialized())
for player_data in players_list:
    player_table.insert(Player.player_serialized(player_data))
for p in player_table:
    players_list.append(Player.deserialize_player())
for player in players_list:
    print(player.player_serialized(Player))
for tournament_data in tournament_list:
    tournament_table.insert(tournament_data.tournament_serialized())
for t in tournament_table:
    tournament_list.append(Tournament.deserialize_tournament())
for tournament in tournament_list:
    print(tournament.tournament_serialized())"""

controler = HomeController()
controler.display_main_page()

