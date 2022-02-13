""" views """
from views.base import Views

""" modeles """
from models import *
from models.player import Player
from models.tournament import TournamentSwiss
from models.round import Round
from models.match import Match

""" controller """
from controller.controller import Controller

def main():
	views = Views()
	game = Controller(views, TournamentSwiss)
	game.welcome_page()
	game.main_menu()

if __name__ == "__main__":
	main()

	