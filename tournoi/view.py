from datetime import datetime
import os

os.system("")


class Colors:

    HEADER = '\033[35m'
    OKBLUE = '\033[34m'
    OKCYAN = '\033[36m'
    OKGREEN = '\033[32m'
    STR_YELLOW = '\033[33m'
    FAIL = '\033[31m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    vert = OKGREEN + BOLD
    ligne = HEADER + UNDERLINE
    design = f"{STR_YELLOW + BOLD} |----------| {ENDC}"
    d_red_vs = f"{FAIL + BOLD} -- VS -- {ENDC}"
    d_red = f"{FAIL + BOLD} |----------| {ENDC}"
    d_red_2 = f"{FAIL + BOLD} |===== Pour =====| {ENDC}"


class TournamentView:

    def display_create_tournament(self):
        name = input("\n"f"{Colors.HEADER}Nom du tournoi: {Colors.OKBLUE}")
        place = input(f"{Colors.HEADER}Lieu du tournoi: {Colors.OKBLUE}")
        date = None
        while date is None:
            try:
                date_input = [int(v) for v in input(f"{Colors.HEADER}Date (jj/mm/aaaa): {Colors.OKBLUE}").split("/")]
                date = datetime(date_input[2], date_input[1], date_input[0]).date()
            except (ValueError, IndexError):
                print(f"{Colors.FAIL}La date n'est pas valide ! ")
        nb_round = int(input(f"{Colors.HEADER}Combien de tours ?: {Colors.OKBLUE}") or "4")
        time_control = None
        while time_control not in ["bu", "bl", "cr"]:
            time_control = input(f"{Colors.HEADER}veuillez saisir 'bu, bl ou cr': {Colors.OKBLUE}")
        description = input(f"{Colors.HEADER}description du tournoi: {Colors.OKBLUE}")
        nb_players = int(input(f"{Colors.HEADER}Combien de joueurs ?: {Colors.OKBLUE}") or "8")

        return (name, place, date.strftime("%d-%m-%Y"), nb_round,
                time_control, description, nb_players)

    def display_all_tournaments(self, tournament_list):
        for i, tournament in enumerate(tournament_list):
            print(f"{Colors.OKCYAN} - {Colors.STR_YELLOW}Selection du tournoi à afficher: ")
            while tournament.name not in tournament.name:
                print("Veuillez saisir un chiffre de tournoi", tournament.name)
            print(f" {Colors.OKCYAN}{i} {Colors.OKGREEN}{tournament.name}""\n")
        return int(input(f"{Colors.STR_YELLOW}Quel est votre choix: "))

    def view_details_tournament(self, tournament):
        print("\n"f"{Colors.STR_YELLOW}Liste des joueurs: ""\n")
        for player in tournament.players:
            print(f"{Colors.OKCYAN} * {Colors.OKGREEN}{player.first_name} {player.last_name}{Colors.ENDC}""\n")
        print("\n"f"{Colors.STR_YELLOW}Nombre de tours: {Colors.OKGREEN}{tournament.nb_round}")
        print(f"{Colors.STR_YELLOW}Liste des tours d'un tournoi: ""\n")
        for i, round_info in enumerate(tournament.rounds, start=1):
            for player_round in round_info.matchs:
                player_1 = f"{Colors.OKGREEN}{player_round.player1}"
                player_2 = f"{Colors.OKGREEN}{player_round.player2}"
                print(f"{Colors.OKCYAN}- {i} {player_1} {Colors.d_red_vs} {player_2}""\n")
        print(f"{Colors.STR_YELLOW}Classement des joueurs: ""\n")
        for rank in tournament.players:
            player_position = f"{Colors.OKGREEN}{rank.position} {Colors.FAIL} points"
            player_first_name = f"{Colors.OKCYAN}* {Colors.OKGREEN}{rank.first_name}"
            print((f"{Colors.OKCYAN}* {player_position} {Colors.design} {player_first_name}"))
        print("\n"f"{Colors.STR_YELLOW}Liste des matchs: {Colors.ENDC}""\n")
        for t_round in tournament.rounds:
            for match in t_round.matchs:
                print(f"{Colors.OKGREEN}{match.player1}{Colors.d_red_vs} {Colors.OKGREEN}{match.player2}{Colors.ENDC}")


class HomeView:

    def display_home(self):
        print("\n"f"{Colors.OKCYAN + Colors.BOLD}'l' {Colors.STR_YELLOW}Pour créer un tournoi: ""\n")
        print(f"{Colors.OKCYAN + Colors.BOLD}'B' {Colors.STR_YELLOW}Afficher la liste des tournois: ""\n")
        print(f"{Colors.OKCYAN + Colors.BOLD}'Y' {Colors.STR_YELLOW}Afficher les acteurs par ordre aphabétique: ""\n")
        print(f"{Colors.OKCYAN + Colors.BOLD}'T' {Colors.STR_YELLOW}Afficher les acteurs par classement: ""\n")
        print(f"{Colors.OKCYAN + Colors.BOLD}'Q' {Colors.STR_YELLOW}Quitter l'application: ""\n")
        return input(f"{Colors.ligne}{Colors.BOLD}Quel est votre choix ?{Colors.ENDC}: {Colors.OKBLUE}")


class PlayerView:

    def display_create_user(self):
        first_name = input("\n"f"{Colors.HEADER}Prenom{Colors.ENDC}: {Colors.OKBLUE}")
        last_name = input(f"{Colors.HEADER}Nom{Colors.ENDC}: {Colors.OKBLUE}")
        date_of_birth = input(f"{Colors.HEADER}Date de naissance{Colors.ENDC}: {Colors.OKBLUE}")
        gender = input(f"{Colors.HEADER}Genre{Colors.ENDC}: {Colors.OKBLUE}")

        return first_name.capitalize(), last_name.capitalize(), date_of_birth, gender


class RoundView:

    def display_round(self, my_round):
        print("\n"f"{Colors.UNDERLINE}{Colors.HEADER}Detail du match {Colors.ENDC}: ""\n")
        for match in my_round.matchs:
            print(f"{Colors.vert}{match.player1} {Colors.d_red_vs} {Colors.vert}{match.player2}{Colors.ENDC}")


class MatchView:


    def display_match(self, my_match):
        for match in my_match.matchs:
            print("\n"f"{Colors.OKGREEN}{match.round}")

    def get_score(self, match):
        print("\n"f"{Colors.HEADER}Tapez 1: {Colors.OKBLUE}{match.player1}{Colors.HEADER} Gagnant(e) + 1 Point")
        print(f"{Colors.HEADER}Tapez 2: {Colors.OKBLUE}{match.player2}{Colors.HEADER} Gagnant(e) + 1 Point")
        print(f"{Colors.HEADER}Tapez 0 pour égalité + 0.5 Point {Colors.OKBLUE}""\n")
        return int(input(f"{Colors.UNDERLINE}{Colors.HEADER}Quel est votre choix ?{Colors.ENDC}: {Colors.OKBLUE}"))

    def display_ranking(self, tournament):
        tournament.players.sort(key=lambda x: x.position, reverse=True)
        print("\n"f"{Colors.UNDERLINE}{Colors.HEADER}Position des acteurs du tournoi par points{Colors.ENDC}: ""\n")
        for player in tournament.players:
            player_position = f"{Colors.OKGREEN}{player.position} Points{Colors.ENDC}"
            print(f"{Colors.OKCYAN}* {Colors.vert}{player} {Colors.d_red} {player_position}")
        tournament.players.sort(key=lambda x: x.first_name)
        info_player = "Liste des acteurs du tournoi par ordre alphabétique"
        print("\n"f"{Colors.UNDERLINE}{Colors.HEADER}{info_player}{Colors.ENDC}: {Colors.HEADER}""\n")
        for player in tournament.players:
            print(f"* {Colors.OKGREEN}{player}""\n")


class SortPlayer:

    def display_sort_players(self, player_list):
        for player in player_list:
            players = f"{Colors.OKCYAN}* {Colors.OKGREEN}{player.first_name}"
            print(f"{players}""\n")

    def display_sort_points(self, player_list):
        for player_points in player_list:
            player_name = f"{Colors.OKGREEN}{player_points.first_name}"
            player_point = f"{Colors.OKGREEN}{player_points.position}"
            players = f"{Colors.OKCYAN}* {player_point} Points {Colors.d_red_2} {player_name}"
            print(f"{players}""\n")
