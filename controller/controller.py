
from models.player import Player
from models.tournament import TournamentSwiss, TIME_CONTROLE_STANDARD
from models.property import Property, DateProperty
from string import ascii_lowercase, ascii_uppercase
import os

STRING_TESTING = ascii_lowercase + ascii_uppercase + " -_"
class Controller:
	"""controlleur principal """

	def __init__(self, views, tournament):
		self._tournament_cls = tournament
		self.tournament = None
		self.views = views

	def welcome_page(self):
		print("welcome page")
		self.views.welcome_page()

	def main_menu(self):
		MENU_ITEM_DICT = {
			"Creation d'un nouveau tournois" : self.start_new_tournament,
			"Ajout d'un nouveau joueur" : self.add_player,
			"Charger un tournois précedent" : self.views.not_implemented,
			"Importer un joueur" : self.views.not_implemented,
			"Quitter" : self.quit
			}
		#get the list of item for the main menu
		menu_item_list = [x for x in MENU_ITEM_DICT.keys()]

		#get the answer from the user
		user_answer = self.views.main_menu_page(menu_item_list)-1
		print(user_answer)
		print(menu_item_list)
		# convert the answer to the function 
		function_called_by_user = MENU_ITEM_DICT[menu_item_list[user_answer]]
		# Call the function
		function_called_by_user()

	def start_new_tournament(self):
		""" creation des property pour la creation de tournois"""
		name = Property("Nom : ")
		location = Property("Lieu : ")
		location.set_control(lambda x: x.isalpha(), 
			"introduite seulement des lettres merci")
		date = DateProperty("Date (JJ/MM/YYYY): ")
		duration = Property("Durée : ")
		duration.set_control(lambda x: x.isnumeric(),
			"introduire seulement un nombre entier de jours")
		round_nbr = Property("Nombre de tours (defaut 4) : ")
		round_nbr.set_control(lambda x: x.isnumeric(),
			"introduire seulement un nombre entier de tours")
		prelim_text = "Quel gestion du temps voullez vous appliquer ? :"
		text = "choix : "
		time_control = MultipleChoicesProperty(prelim_text, 
			TIME_CONTROLE_STANDARD, text)
		description = Property("Desciption : \n")
		""" envoie des proprety à la vue """
		parameter_list = [name, location, date, duration, 
		round_nbr, time_control, description]
		tournament_data = self.views.get_tournament_data(parameter_list)
		""" creation de tournois """	
		self.tournament = self._tournament_cls(**tournament_data)
		self.views.tournament_created(self.tournament)
		self.main_menu()

	def add_player(self):
		if self.tournament:
			if self.tournament.isFull():
				self.views.max_number_players_reach()
				self.main_menu()
			else:
				player_data = self.views.new_player_page()
				newPlayer = Player(**player_data)
				self.tournament.addPlayer(newPlayer)
				self.main_menu()
		else:
			self.views.ask_to_create_tournament()
			self.main_menu()
		
	def group_generation(self):
		self.tournament.player_group_generation()

	def end_round(self):
		#self.tournament
		pass

	def quit(self):
		self.views.exit_message()
		exit()

if __name__ == "__main__":
	pass
