from tournoi.models import Tournament, Player, tournament_list, players_list
import settings
from tinydb import TinyDB


def get_current_tournament():
    load_db = TinyDB(settings.DB_NAME)
    load_table = load_db.table(settings.TABLE_CURRENT_TOURNAMENT)
    if not load_table:
        return
    tournament = Tournament.deserialize(load_table.all()[0])
    return tournament


def current_tournament_finished():
    load_db = TinyDB(settings.DB_NAME)
    load_table = load_db.table(settings.TABLE_CURRENT_TOURNAMENT)
    load_table.truncate()


def load_tournament():
    load_db = TinyDB(settings.DB_NAME)
    tournament_table = load_db.table(settings.TABLE_TOURNAMENT)
    player_table = load_db.table(settings.TABLE_PLAYER)

    for t in tournament_table:
        tournament_list.append(Tournament.deserialize(t))

    for p in player_table:
        players_list.append(Player.deserialize(p))
