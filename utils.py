from tournoi.models import Tournament, Player, tournament_list, players_list
from tinydb import TinyDB


def get_current_tournament():
    load_db = TinyDB("db_current_tournament.json")
    load_table = load_db.table("current_tournament")
    if not load_table:
        return
    tournament = Tournament.deserialize(load_table.all()[0])
    return tournament


def load_tournament():
    load_db = TinyDB("db.json")
    load_table = load_db.table("tournaments")
    load_db_player = TinyDB("player_db.json")
    load_table_player = load_db_player.table("players")
    for p in load_table_player:
        players_list.append(Player.deserialize(p))
    for player in players_list:
        print(player.serialize())
    for t in load_table:
        tournament_list.append(Tournament.deserialize(t))
    for tournament in tournament_list:
        print(tournament.serialize())