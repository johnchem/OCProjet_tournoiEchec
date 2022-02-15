""" views """
from views.base import Views

""" modeles """
from models.player import Player
from models.tournament import TournamentSwiss
from models.round import Round
from models.match import Match

""" controller """
from controller.controller import Controller

def main(database_name):
	views = Views()
	game = Controller(views, TournamentSwiss, database_name)
	game.welcome_page()
	game.main_menu()

if __name__ == "__main__":
	DB_FILE_NAME = "DB_test.json" # name of the file
	main(DB_FILE_NAME)

	