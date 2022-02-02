
from models.player import Player
import os

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
		print("test start function")
		tournament_data = self.views.get_tournament_data()
		self.tournament = self._tournament_cls(**tournament_data)
		self.views.tournament_created(self.tournament)
		self.main_menu()

	def add_player(self):
		if self.tournament:
			print("oups j'ai rien à faire là")
			if self.tournament.isFull():
				self.view.max_number_players_reach()
				self.main_menu()
			else:
				player_data = self.views.new_player_page()
				newPlayer = player.joueur(**player_data)
				self.tournament.addPlayer(newPlayer)
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
