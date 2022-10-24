from tournoi.controlers import HomeController
from utils import load_tournament

load_tournament()
controler = HomeController()
controler.display_main_page()

#print(tournament_load(tournament_list))

