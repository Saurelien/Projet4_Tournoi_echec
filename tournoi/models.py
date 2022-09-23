from tinydb import TinyDB

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

    def tournament_finalized(self):
        tournament_list.append(self)

    def tournament_serialized(self):
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
            data["players"].append(player.player_serialized())
        for data_tournament in self.rounds:
            data["rounds"].append(data_tournament.round_serialized())
        tournament_db = TinyDB("tournament_db.json")
        tournament_table = tournament_db.table("tournaments")
        tournament_table.truncate()
        tournament_table.insert(data)
        return data

    @classmethod
    def deserialize_tournament(cls, data):
        tournament_cls = cls(data["name"], data["place"], data["date"],
                             data["nb_round"], data["time_control"],
                             data["description"], data["nb_players"])
        tournament_cls.place = data["place"]
        tournament_cls.date = data["date"]
        tournament_cls.nb_round = data["nb_round"]
        tournament_cls.time_control = data["time_control"]
        tournament_cls.description = data["description"]
        tournament_cls.nb_players = data["nb_players"]
        for round_info in data["rounds"]:
            tournament_cls.add_round(Round.deserialize_round(round_info))
        for player_info in data["players"]:
            tournament_cls.add_player(Player.deserialize_player(player_info))
        return tournament_cls


class Player:

    def __init__(self, first_name, last_name, date_of_birth, gender, *args, **kwargs):
        super().__init__(*args, **kwargs)
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

    def player_finalized(self):
        players_list.append(self)

    def player_serialized(self):
        return {
                 "first_name": self.first_name,
                 "last_name": self.last_name,
                 "date_of_birth": self.date_of_birth,
                 "gender": self.gender,
                 "position": self.position
                }

    @classmethod
    def deserialize_player(cls, data):
        return cls(data["first_name"],
                   data["last_name"],
                   data["date_of_birth"],
                   data["gender"],
                   data["position"])


class Match:

    def __init__(self, player1, player2):
        """Correspond à deux joueurs qui s'affrontent par match"""
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
    def deserialize_round(cls, data):
        round_tournament = cls(data["tournament"])
        round_tournament.name = data["tournament"]
        for match_info in data["matchs"]:
            round_tournament.add_match(Match.deserialize_match(match_info))
        return round_tournament

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
