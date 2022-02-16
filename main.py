""" views """
from chess_tournament.views.base import Views

""" modeles """
from chess_tournament.models.player import Player
from chess_tournament.models.tournament import TournamentSwiss
from chess_tournament.models.round import Round
from chess_tournament.models.match import Match

""" controller """
from chess_tournament.controller.controller import Controller

def main(database_name):
	views = Views()
	game = Controller(views, TournamentSwiss, database_name)
	game.welcome_page()
	game.main_menu()

if __name__ == "__main__":
	DB_FILE_NAME = "DB_test.json" # name of the file
	main(DB_FILE_NAME)

	