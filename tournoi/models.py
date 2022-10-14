from tinydb import TinyDB

players_list = []
tournament_list = []
current_tournament = []


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
            print(player.position)
            for a_round in self.rounds:
                print(player.position)
                for a_match in a_round.matchs:
                    print(a_match.player1, a_match.score_p1, "---------", a_match.player2, a_match.score_p2)
                    print()
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
            tournament_table.insert(tournament.serialize())

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
            data["rounds"].append(data_tournament.round_serialized())
        return data
    """.strptime("%d-%m-%Y")"""

    @classmethod
    def deserialize(cls, data):
        tournament = cls(data["name"],
                         data["place"],
                         data["date"],
                         data["nb_round"],
                         data["time_control"],
                         data["description"],
                         data["nb_players"])
        for round_info in data["rounds"]:
            tournament.add_round(Round.deserialize(round_info))
        for player_info in data["players"]:
            tournament.add_player(Player.deserialize(player_info))
        return tournament

    def check_step(self):
        current_db = TinyDB("current_t.json")
        current_table = current_db.table("current_tournament")
        current_table.truncate()
        

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

    def save(self):
        players_list.append(self)
        db = TinyDB("player_db.json")
        db_table = db.table("players")
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
        self.score_p1 = int(0)
        self.score_p2 = int(0)

    def match_serialized(self):
        return {
                "player1": self.player1.serialize(),
                "player2": self.player2.serialize(),
                "score_p1": self.score_p1,
                "score_p2": self.score_p2
                }

    @classmethod
    def deserialize(cls, data):
        instance = cls(Player.deserialize(data["player1"]),
                       Player.deserialize(data["player2"]))
        instance.score_p1 = data["score_p1"]
        instance.score_p2 = data["score_p2"]
        return instance.score_p1, instance.score_p2


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
        instance = cls()
        for match_info in data["matchs"]:
            instance.add_match(Match.deserialize(match_info))
        return instance
    
    def generate_pair(self):
        self.tournament.players.sort(key=lambda x: x.position)
        spliting = len(self.tournament.players)
        #list = self.tournament.players
        middle_index = spliting // 2
        superior_list = self.tournament.players[:middle_index]
        inferior_list = self.tournament.players[middle_index:]
        #pairing = [(a, b) for id, a in enumerate(list) for b in list[id +1:]]
        for i, player1 in enumerate(superior_list):
            player2 = inferior_list[i - 1]
            match = Match(player1, player2)
            self.add_match(match)
        """player1 = superior_list
        player2 = inferior_list
        pairing = [(a, b) for a in player1 for b in player2 if a != b]
        match = Match(player1, player2)
        self.add_match(match)"""
