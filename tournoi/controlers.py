from .models import Player, Round, Tournament, players_list, tournament_list
from .view import (HomeView, PlayerView, SortPlayer,
                   RoundView, TournamentView, MatchView, Colors)

colors = Colors()


class HomeController:
    
    def create_tournament(self):
        tournament_controller = TournamentController()
        player_controler = PlayerController()
        tournament = tournament_controller.create_tournament_controler()

        for i in range(int(tournament.nb_players)):
            player = player_controler.create_user()
            player.save()
            player.serialize()
            tournament.add_player(player)
        view_round = RoundView()
        for j in range(int(tournament.nb_round)):
            t_round = Round()
            tournament.add_round(t_round)
            t_round.generate_pair()
            print(tournament.players)
            view_round.display_round(t_round)
            match_view = MatchView()
            for match in t_round.matchs:
                winner = match_view.get_score(match)
                if winner == 1:
                    match.score_p1 = 1
                elif winner == 2:
                    match.score_p2 = 1
                else:
                    match.score_p1 = 0.5
                    match.score_p2 = 0.5
            tournament.update_score()
            match_view.display_ranking(tournament)
        tournament.save()
        tournament.serialize()

    def display_main_page(self):
        main = HomeView()
        home = HomeController()
        report = ReportController()
        exit = False
        while exit is False:
            choice = main.display_home()
            if choice == "l":
                print("\n"f"{colors.STR_YELLOW + colors.BOLD}veuillez remplir les champs requis: ""\n")
                home.create_tournament()
            elif choice == "B" or choice == "b":
                print("\n"f"{colors.STR_YELLOW + colors.BOLD}Liste des tournois{colors.ENDC}: ""\n")
                report.tournament_detail()
            elif choice == "Y" or choice == "y":
                print("\n"f"{colors.STR_YELLOW + colors.BOLD}Participants par ordre alphabétique{colors.ENDC}: ""\n")
                report.create_report_alpha()
            elif choice == "T" or choice == "t":
                print("\n"f"{colors.STR_YELLOW + colors.BOLD}Participants par nombre de points{colors.ENDC}: ""\n")
                report.create_report_points()
            elif choice == "Q" or choice == "q":
                exit = True
                print("\n"f"{colors.STR_YELLOW}Vous avez quitté l'application avec succès !")


class ReportController:

    def create_report_alpha(self):
        view_sort = SortPlayer()
        view_sort.display_sort_players(sorted(players_list,
                                              key=lambda x: (x.first_name
                                                             ,x.last_name)))

    def create_report_points(self):
        view_points = SortPlayer()
        view_points.display_sort_points(sorted(players_list,
                                        key=lambda x: x.position
                                        ,reverse=True))

    def tournament_detail(self):
        tournament_list_view = TournamentView()
        choice = tournament_list_view.display_all_tournaments(sorted(tournament_list, key=lambda x: x.name))
        tournament_list_view.view_details_tournament(tournament_list[choice])


class PlayerController:

    def create_user(self):
        view = PlayerView()
        first_name, last_name, date_of_birth, gender = view.display_create_user()
        return Player(first_name, last_name, date_of_birth, gender)


class TournamentController:

    def create_tournament_controler(self):
        tournament_view = TournamentView()
        (name, place, date, nb_round, time_control,
         description, nb_players) = tournament_view.display_create_tournament()
        new_tournament = Tournament(name, place, date, nb_round, time_control, description, nb_players)
        return new_tournament
