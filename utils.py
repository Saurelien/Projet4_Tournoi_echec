from tournoi.models import Tournament
from tinydb import TinyDB


def get_current_tournament():
    load_db = TinyDB("db_current_tournament.json")
    load_table = load_db.table("current_tournament")
    if not load_table:
        return
    tournament = Tournament.deserialize(load_table.all()[0])
    return tournament
