from tinydb import TinyDB

players_list = []
tournament_list = []
current_tournament = []


class Tournament:

    def __init__(self, name, place, date, nb_round, time_control,
                 description, nb_players, *args, **kwargs):
        super().__init__()
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

    def __str__(self):
        return (self.name, self.place, self.date,
                self.nb_round, self.time_control, self.description)

    def update_score(self):
        for player in self.players:
            for a_round in self.rounds:
                for a_match in a_round.matchs:
                    if a_match.player1 == player:
                        player.position += a_match.score_p1
                    elif a_match.player2 == player:
                        player.position += a_match.score_p2

    def save(self):
        tournament_list.append(self)
        tournament_db = TinyDB("db.json")
        tournament_table = tournament_db.table("tournaments")
        tournament_table.truncate()
        for tournament in tournament_list:
            tournament_table.insert(tournament.serialized())

    def serialized(self):
        data = {
                    "name": self.name,
                    "place": self.place,
                    "date": self.date.strftime("%d-%m-%Y"),
                    "rounds": list(),
                    "nb_round": self.nb_round,
                    "time_control": self.time_control,
                    "description": self.description,
                    "nb_players": self.nb_players,
                    "players": list()
                }
        for player in self.players:
            data["players"].append(player.serialized())
        for data_tournament in self.rounds:
            data["rounds"].append(data_tournament.round_serialized())
        return data

    @classmethod
    def deserialize(cls, data):
        tournament = cls(data["name"]
                         , data["place"]
                         , data["date"]
                         , data["nb_round"]
                         , data["time_control"]
                         , data["description"]
                         , data["nb_players"])
        tournament.place = data["place"]
        tournament.date = data["date"]
        for round_info in data["rounds"]:
            tournament.add_round(Round.deserialize(round_info))
        tournament.nb_round = data["nb_round"]
        tournament.time_control = data["time_control"]
        tournament.description = data["description"]
        tournament.nb_players = data["nb_players"]
        for player_info in data["players"]:
            tournament.add_player(Player.deserialize(player_info))
        return type(tournament)

    def check_step(self):
        pass

class Player:

    def __init__(self, first_name, last_name, date_of_birth, gender, *args, **kwargs):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.position = 0

    def all_user_info(self):
        return (self.first_name, self.last_name, self.date_of_birth,
                self.gender, self.position, self.players)

    def __str__(self):
        return self.first_name

    def save(self):
        players_list.append(self)
        db = TinyDB("player_db.json")
        db_table = db.table("players")
        db_table.truncate()
        for player in players_list:
            db_table.insert(player.serialized()) 

    def serialized(self):
        return {
                 "first_name": self.first_name,
                 "last_name": self.last_name,
                 "date_of_birth": self.date_of_birth,
                 "gender": self.gender,
                 "position": self.position
                }

    @classmethod
    def deserialize(cls, data):
        return cls(data["first_name"]
                   , data["last_name"]
                   , data["date_of_birth"]
                   , data["gender"]
                   , data["position"])


class Match:

    def __init__(self, player1, player2):
        self.round = None
        self.player1 = player1
        self.player2 = player2
        self.score_p1 = 0
        self.score_p2 = 0

    def match_serialized(self):
        return {
                "player1": self.player1.first_name,
                "player2": self.player2.first_name,
                "score_p1": self.score_p1,
                "score_p2": self.score_p2
                }

    @classmethod
    def deserialize_match(cls, data):
        return cls(data["player1"],
                   data["player2"],
                   data["score_p1"],
                   data["score_p2"])


class Round:

    def __init__(self):
        self.tournament = None
        self.matchs = list()

    def add_match(self, match):
        self.matchs.append(match)
        match.round = self

    def round_serialized(self):
        data = {
                "tournament": self.tournament.name,
                "matchs": list()
                }
        for data_round in self.matchs:
            data["matchs"].append(data_round.match_serialized())
        return data

    @classmethod
    def deserialize(cls, data):
        for match_info in cls(data["matchs"]):
            Round.add_match(Match.deserialize_match(match_info))

    def generate_pair(self):
        self.tournament.players.sort(key=lambda x: x.position)
        spliting = len(self.tournament.players)
        middle_index = spliting // 2
        superior_list = self.tournament.players[:middle_index]
        inferior_list = self.tournament.players[middle_index:]
        for i, player1 in enumerate(superior_list):
            player2 = inferior_list[i]
            match = Match(player1, player2)
            self.add_match(match)
