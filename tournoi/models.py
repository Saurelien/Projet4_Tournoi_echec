from tinydb import TinyDB
import settings
players_list = []
tournament_list = []
current_tournament = None


class Tournament:

    def __init__(self, name, place, date, nb_round, time_control,
                 description, nb_players, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.place = place
        self.date = date
        self.rounds = list()
        self.nb_round = nb_round
        self.time_control = time_control
        self.description = description
        self.nb_players = nb_players
        self.players = list()

    def add_player(self, players):
        self.players.append(players)
        players.tournament = self

    def add_round(self, round_1):
        self.rounds.append(round_1)
        round_1.tournament = self

    def save(self, current=False):
        if current:
            tournament_db = TinyDB(settings.DB_NAME)
            current_tournament_table = tournament_db.table(settings.TABLE_CURRENT_TOURNAMENT)
            current_tournament_table.truncate()
            current_tournament_table.insert(self.serialize())
            return
        tournament_list.append(self)
        tournament_db = TinyDB(settings.DB_NAME)
        tournament_table = tournament_db.table(settings.TABLE_TOURNAMENT)
        tournament_table.truncate()
        for tournament in tournament_list:
            tournament_table.insert(tournament.serialize())
        for player in self.players:
            player.save()

    def serialize(self):
        data = {
                    "name": self.name,
                    "place": self.place,
                    "date": self.date,
                    "rounds": list(),
                    "nb_round": self.nb_round,
                    "time_control": self.time_control,
                    "description": self.description,
                    "nb_players": self.nb_players,
                    "players": list()
                }
        for player in self.players:
            data["players"].append(player.serialize())
        for data_tournament in self.rounds:
            data["rounds"].append(data_tournament.serialize())
        return data

    @classmethod
    def deserialize(cls, data):
        tournament = cls(data["name"],
                         data["place"],
                         data["date"],
                         data["nb_round"],
                         data["time_control"],
                         data["description"],
                         data["nb_players"])
        print(tournament.nb_round)
        for player_info in data["players"]:
            tournament.add_player(Player.deserialize(player_info))
        for round_info in data["rounds"]:
            tournament.add_round(Round.deserialize(round_info))
        return tournament


class Player:

    def __init__(self, first_name, last_name, date_of_birth, gender, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.position = 0

    """def all_user_info(self):
        return (self.first_name, self.last_name, self.date_of_birth,
                self.gender, self.position, self.players)"""

    def __str__(self):
        return self.first_name

    def save(self):
        players_list.append(self)
        db = TinyDB(settings.DB_NAME)
        db_table = db.table(settings.TABLE_PLAYER)
        db_table.truncate()
        for player in players_list:
            db_table.insert(player.serialize())

    def serialize(self):
        return {
                 "first_name": self.first_name,
                 "last_name": self.last_name,
                 "date_of_birth": self.date_of_birth,
                 "gender": self.gender,
                 "position": self.position
                }

    @classmethod
    def deserialize(cls, data):
        instance = cls(data["first_name"],
                       data["last_name"],
                       data["date_of_birth"],
                       data["gender"])
        instance.position = data["position"]
        return instance


class Match:

    def __init__(self, player1, player2):
        self.round = None
        self.player1 = player1
        self.player2 = player2
        self.score_p1 = 0
        self.score_p2 = 0

    def serialize(self):
        return {
                "player1": self.player1.serialize(),
                "player2": self.player2.serialize(),
                "score_p1": self.score_p1,
                "score_p2": self.score_p2
                }

    @classmethod
    def deserialize(cls, data):
        instance = cls(Player.deserialize(data["player1"]),
                       Player.deserialize(data["player2"]),)
        instance.score_p1 = data["score_p1"]
        instance.score_p2 = data["score_p2"]
        return instance

    def set_winner(self, winner):
        if winner == 1:
            self.score_p1 = 1
            self.player1.position += 1
        elif winner == 2:
            self.score_p2 = 1
            self.player2.position += 1
        else:
            self.score_p1 = 0.5
            self.player1.position += 0.5
            self.score_p2 = 0.5
            self.player2.position += 0.5


class Round:

    def __init__(self):
        self.tournament = None
        self.matchs = list()

    def add_match(self, match):
        self.matchs.append(match)
        match.round = self

    def serialize(self):
        data = {
                "matchs": list()
                }
        for data_round in self.matchs:
            data["matchs"].append(data_round.serialize())
        return data

    @classmethod
    def deserialize(cls, data):
        instance = cls()
        for match_info in data["matchs"]:
            instance.add_match(Match.deserialize(match_info))
        return instance

    def generate_pair(self):
        self.tournament.players.sort(key=lambda x: x.position)
        spliting = len(self.tournament.players)
        middle_index = spliting // 2
        superior_list = self.tournament.players[:middle_index]
        inferior_list = self.tournament.players[middle_index:]
        for i, player1 in enumerate(superior_list):
            player2 = inferior_list[i - 1]
            match = Match(player1, player2)
            self.add_match(match)

