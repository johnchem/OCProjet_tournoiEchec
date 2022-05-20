
from chess_tournament.models.player import Player
from chess_tournament.models.tournament import TIME_CONTROLE_STANDARD
from chess_tournament.models.round import Round
from chess_tournament.models.match import Match
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
		self.views.welcome_page()

	def main_menu(self):
		if self.tournament is not None:
			save_result, data, player_id = save_tournament_data(self.tournament.serialize(), self.DB_ADDRESS)
			if save_result:
				self.tournament.id=data
			else :
				self.views.error_save_page(data)
			
			if player_id:
				for player, value in zip(self.tournament.players, player_id):
					player.id = value

		MENU_ITEM_DICT = {
			"Cloture du tour actuel" : self.stop_current_round,
			"Cloture du tournois" : self.tournament_closure,
			"Commencer un nouveau tour" : self.start_new_round,
			"Creation d'un nouveau tournois" : self.start_new_tournament,
			"Ajout d'un nouveau joueur" : self.add_player,
			"Modification classement d'un joueur" : self.change_player_rank,
			"Charger un tournois précedent" : self.load_tournament,
			"Importer un joueur" : self.load_player,
			"Quitter" : self.quit
			}

		#remove forbidden element
		if self.tournament is None:
			MENU_ITEM_DICT.pop("Cloture du tour actuel", None)
			MENU_ITEM_DICT.pop("Cloture du tournois", None)
			MENU_ITEM_DICT.pop("Commencer un nouveau tour", None)
			MENU_ITEM_DICT.pop("Ajout d'un nouveau joueur", None)
			MENU_ITEM_DICT.pop("Importer un joueur",None)
			MENU_ITEM_DICT.pop("Modification classement d'un joueur", None)
		else:			
			if self.tournament.is_full():
				MENU_ITEM_DICT.pop("Ajout d'un nouveau joueur", None)
				MENU_ITEM_DICT.pop("Importer un joueur",None)

			if self.tournament.current_round < self.tournament.number_of_round:
				MENU_ITEM_DICT.pop("Cloture du tournois", None)
			else :
				MENU_ITEM_DICT.pop("Commencer un nouveau tour", None)
				
			if len(self.tournament.rounds) == 0:
				MENU_ITEM_DICT.pop("Cloture du tour actuel", None)
			elif self.tournament.rounds[-1].is_done:
				MENU_ITEM_DICT.pop("Cloture du tour actuel", None)
			else:
				MENU_ITEM_DICT.pop("Cloture du tournois", None)

		#get the list of item for the main menu
		menu_item_list = [x for x in MENU_ITEM_DICT.keys()]

		#get the answer from the user
		if self.tournament:
			current_round_name = None
			if not len(self.tournament.rounds) == 0:
				current_round_name = self.tournament.rounds[-1].name
			
			user_answer = self.views.main_menu_page(menu_item_list, 
				tournament_name = self.tournament.name,
				player_nb = len(self.tournament.players),
				current_round_name=current_round_name
				)-1
		else:	
			user_answer = self.views.main_menu_page(menu_item_list)-1
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
		save_result, err, _ = save_tournament_data(self.tournament.serialize(), self.DB_ADDRESS)
		if save_result:
			self.views.save_performed_page()
		else :
			self.views.error_save_page(err)

	def tournament_closure(self):
		self.views.grille_americaine(self.tournament)
		self.main_menu()

	def add_player(self):
		# controle la présence d'un tournois actif
		if self.tournament:
			# controle si on peut ajouter des joueurs
			if self.tournament.is_full():
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
				new_player = Player(**player_data)
				self.tournament.add_player(new_player)

				""" sauvegarde du joueur dans la db joueur"""
				save_result, data = save_player_data(new_player.serialize(), self.DB_ADDRESS)
				if save_result:
					new_player.id = data
					self.views.save_performed_page()
				else :
					self.views.error_save_page(data)
				
				self.main_menu()
		else:
			self.views.ask_to_create_tournament()
			self.main_menu()
		
	def change_player_rank(self):
		# mise en forme et affichage des joueurs sauvegardés
		player_name_formated = []
		for player in self.tournament.players:
			player_name_formated.append(f"{player.forname} {player.name}")
		
		#reception du choix de l'utilisateur
		user_choices = self.views.load_player_page(player_name_formated)
		chosen_player = self.tournament.players[user_choices-1]
		
		# modification des données
		rank = Property()
		rank.set_message("Nouveau classement :")
		rank.set_defaut_value(int(chosen_player.rank))
		chosen_player.rank = self.views.update_player(chosen_player, rank)

		""" sauvegarde du joueur dans la db joueur"""
		save_result, data = save_player_data(chosen_player.serialize(), self.DB_ADDRESS)
		if save_result:
			chosen_player.id = data
			self.views.save_performed_page()
		else :
			self.views.error_save_page(data)
		
		self.main_menu()
	
	def load_tournament(self):
		# controle la présence d'une base de données
		if not self.DB_ADDRESS.exists():
			self.views.database_not_found()
			self.main_menu()
		
		# chargement de l'ensemble des tournois enregistré
		history_tournament = load_tournament_data(self.DB_ADDRESS)
		
		# gestion de la reception d'erreur lors de l'importation de la db
		if not isinstance(history_tournament, list):
			self.views.issues_database(history_tournament)
			self.main_menu()

		if len(history_tournament) == 0:
			self.views.no_data_in_db("tournois")
			self.main_menu()

		# mise en forme et affichage les tournois sauvegardés
		tournament_name_formated = self.tournament_historic(history_tournament)
		#reception du choix de l'utilisateur
		user_choices = self.views.load_tournament_page(tournament_name_formated)
		# importation des données
		chosen_tournament = history_tournament[user_choices-1]
		self.tournament = deserialize_tournament(**chosen_tournament)
		self.tournament.get_players_opponent()
		self.tournament.get_players_score()
		self.main_menu()

	def load_player(self):
		# controle la présence d'une base de données
		if not self.DB_ADDRESS.exists():
			self.views.database_not_found()
			self.main_menu()

		# chargement de l'ensemble des joueurs enregistré
		history_players = load_player_data(self.DB_ADDRESS)
		
		# gestion de la reception d'erreur lors de l'importation de la db
		if not isinstance(history_players, list):
			self.views.issues_database(history_players)
			self.main_menu()

		if len(history_players) == 0:
			self.views.no_data_in_db("joueur")
			self.main_menu()

		# mise en forme et affichage des joueurs sauvegardés
		player_name_formated = self.players_historic(history_players)
		#reception du choix de l'utilisateur
		user_choices = self.views.load_player_page(player_name_formated)
		# importation des données
		chosen_player = history_players[user_choices-1]
		self.tournament.add_player(deserialize_player(**chosen_player))
		
		self.main_menu()

	def start_new_round(self):
		player_pairs = self.tournament.start_new_round()
		if player_pairs:
			#definition du nom du round et creation
			current_round = self.tournament.current_round+1
			next_round_name = f'Tour_{current_round}'
			next_round = Round(next_round_name)
			#creation des match et ajout au round
			for x, y in player_pairs:
				new_match = Match(x, y)
				next_round.add_match(new_match)
			self.tournament.rounds.append(next_round)
			self.views.round_recap(next_round)
		else:
			self.views.general_error_message(player_pairs)
		self.main_menu()

	def stop_current_round(self):
		self.tournament.end_round()
		self.views.clear_screen()

		for match in self.tournament.rounds[-1].match:
			result = []
			result = self.views.ask_match_result(match)
			
			while not sum(result) == 1:
				self.views.error_input_match_result()
				result = self.views.ask_match_result(match)

			match.set_result(*result)
		self.tournament.get_players_opponent()
		self.tournament.get_players_score()
		self.views.round_recap(self.tournament.rounds[-1])
		self.main_menu()

	def tournament_historic(self, tournament_list):
		output_list = []
		for tournament in tournament_list:
			output_list.append(f"{tournament['name']}")
		return output_list

	def players_historic(self, players_list):
		output_list = []
		for player in players_list:
			output_list.append(f"{player['forname']} {player['name']}")
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
