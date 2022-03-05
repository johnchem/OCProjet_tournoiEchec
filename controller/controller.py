
from chess_tournament.models.player import Player
from chess_tournament.models.tournament import TournamentSwiss, TIME_CONTROLE_STANDARD
from chess_tournament.models.property import Property
from chess_tournament.models.date_property import DateProperty
from chess_tournament.models.multiple_choices_property import MultipleChoicesProperty
from chess_tournament.models.gender_property import GenderProperty

from chess_tournament.controller.db_manager import save_player_data, load_player_data, \
								save_tournament_data, load_tournament_data
from chess_tournament.controller.deserializer import deserialize_tournament, \
								deserialize_player


from datetime import datetime as dt
from string import ascii_lowercase, ascii_uppercase
import os
import pathlib

STRING_TESTING = ascii_lowercase + ascii_uppercase + " -_"

class Controller:
	"""controlleur principal """

	def __init__(self, views, tournament, database_name):
		self._tournament_cls = tournament
		self.tournament = None
		self.views = views
		self.DB_ADDRESS = pathlib.Path(__file__).parent.absolute().joinpath(database_name) # absolule path

	def welcome_page(self):
		print("welcome page")
		self.views.welcome_page()

	def main_menu(self):
		MENU_ITEM_DICT = {
			"Creation d'un nouveau tournois" : self.start_new_tournament,
			"Ajout d'un nouveau joueur" : self.add_player,
			"Charger un tournois précedent" : self.load_tournament,
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
		name = Property()
		name.set_message("Nom : ")
		
		location = Property()
		location.set_message("Lieu : ")
		location.set_control(lambda x: x.isalpha(), 
			"introduite seulement des lettres merci")
		
		date = DateProperty()
		date.set_message("Date (JJ/MM/YYYY): ")
		
		duration = Property()
		duration.set_message("Durée : ")
		duration.set_control(lambda x: x.isnumeric(),
			"introduire seulement un nombre entier de jours")
		
		round_nbr = Property()
		round_nbr.set_message("Nombre de tours (defaut 4) : ")
		round_nbr.set_control(lambda x: x.isnumeric(),
			"introduire seulement un nombre entier de tours")
		round_nbr.set_defaut_value(4)
		
		prelim_text = "Quel gestion du temps voullez vous appliquer ? :"
		text = "choix : "
		time_control = MultipleChoicesProperty()
		time_control.set_message(prelim_text, TIME_CONTROLE_STANDARD, text)
		
		description = Property()
		description.set_message("Desciption : \n")
		
		""" envoie des proprety à la vue """
		parameter_dict = {"name": name, 
						"location": location, 
						"date": date, 
						"duration": duration,
						"number_of_round": round_nbr,
						"time_control": time_control,
						"description": description}
		tournament_data = self.views.get_tournament_data(parameter_dict)
		
		""" creation de tournois """	
		self.tournament = self._tournament_cls(**tournament_data)
		self.views.tournament_created(self.tournament)
		
		""" sauvegarde du tournois"""
		save_result = save_tournament_data(self.tournament.serialize, self.DB_ADDRESS)
		if save_result:
			self.views.save_performed_page()
		else :
			self.views.error_save_page(save_result)
		self.main_menu()

	def add_player(self):
		# controle la présence d'un tournois actif
		if self.tournament:
			# controle si on peut ajouter des joueurs
			if self.tournament.isFull():
				self.views.max_number_players_reach()
				self.main_menu()
			else:
				# creation des propriétés du nouveau joueur
				name = Property()
				name.set_message("Nom : ")
				forname = Property()
				forname.set_message("Prénom : ")
				gender = GenderProperty()
				gender.set_message("Genre (H/F) : ")
				gender.set_control(lambda x : x in "HF",
					"le genre du joueur doit être H ou F")
				birth_date = DateProperty()
				birth_date.set_message("Date de naissance : ")
				birth_date.set_control(lambda x : (dt.today() - x).days >= 10*365.25,
					"les joueurs doivent avoir plus de 10 ans")
				rank = Property()
				rank.set_message("Classement : ")
				rank.set_defaut_value(0)

				""" envoie des propriétés à la vue"""
				parameter_dict = {"name": name,
					"forname": forname,
					"birth_date": birth_date,
					"gender": gender,
					"rank": rank
				}
				player_data = self.views.new_player_page(parameter_dict)
				""" creation du nouveau joueur"""
				newPlayer = Player(**player_data)
				self.tournament.addPlayer(newPlayer)

				""" sauvegarde du joueur dans la db joueur"""
				if save_player_data(newPlayer.serialize, self.DB_ADDRESS):
					print("joueur sauvegardé")
				self.main_menu()
		else:
			self.views.ask_to_create_tournament()
			self.main_menu()
		
	def load_tournament(self):
		# controle la présence d'une base de données
		if self.DB_ADDRESS.exists():
			print(self.DB_ADDRESS)
			# chargement de l'ensemble des tournois enregistré
			history_tournament = load_tournament_data(self.DB_ADDRESS)
			# gestion de la reception d'erreur lors de l'importation de la db
			print(history_tournament)
			if isinstance(history_tournament, list):
				# mise en forme et affichage les tournois sauvegardés
				tournament_name_formated = self.tournament_historic(history_tournament)
				#reception du choix de l'utilisateur
				user_choices = self.views.load_tournament_page(tournament_name_formated)
				# importation des données 
				print(type(history_tournament[user_choices]))
				self.tournament = deserialize_tournament(history_tournament[user_choices])
			else :
				self.views.issues_database(history_tournament)
				self.main_menu()
		else : 
			self.views.database_not_found()
			self.main_menu()

	def tournament_historic(self, tournament_list):
		output_list = []
		for tournament in tournament_list:
			output_list.append(f"{tournament.name}")
		return output_list

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
