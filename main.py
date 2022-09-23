from tournoi.controlers import HomeController
from tournoi.models import Player, Tournament, tournament_list, players_list
# from tinydb import TinyDB


players_list.append(Player.player_finalized(Player))
tournament_list.append(Tournament.tournament_finalized(Tournament))

tour = list()
player_in_list = list()

for tournament in tour:
    tour.append(Tournament.deserialize_tournament())
    for t in tour:
        print(Tournament.tournament_serialized(t))
controler = HomeController()
controler.display_main_page()