
import os
from models.tournament import TIME_CONTROLE_STANDARD
""" terminal commandes """
CLEAN_SCREEN = "CLS"

class Views:
	""" """

	def __init__(self):
		pass

	def welcome_page(self):
		os.system(CLEAN_SCREEN)
		print("Bienvenue dans Chess Manager")
		os.system("pause")

	def main_menu_page(self, menu_item_list):
		i = 1
		os.system(CLEAN_SCREEN)
		print("________MENU PRINCIPAL________")
		for menu_item in menu_item_list:
			print(f"{i} : {menu_item}")
			i +=1
		return user_choices("indiquer votre choix : ", range(1,i+1))
		
	def get_tournament_data(self, parameter_dict):
		os.system(CLEAN_SCREEN)
		print("CREATION D UN NOUVEAU TOURNOI")
		print("Veuillez remplir les champs ci-dessous \n")
		for item in parameter_dict.values():
			""" demande à l'utilisateur la valeur tant que 
			celle-ci n'est pas conforme """
			while not item.set_value(input(item.message)): pass
		return parameter_dict

	def tournament_created(self, tournois):
		os.system(CLEAN_SCREEN)
		print("Le tournois à bien été crée \n")
		print("Rappel : ")
		print(f"Nom : {tournois.name}")
		print(f"Lieu : {tournois.location}")
		print(f"A partir du {tournois.date.strftime('%d/%m/%Y')} pendant {tournois.duration} jours")
		print(f"{tournois.number_of_round} tours avec la régle {tournois.time_control}")
		print("")
		os.system("pause")

	def new_player_page(self, parameter_dict):
		os.system(CLEAN_SCREEN)
		print("_Creation d'un nouveau joueur_")
		for item in parameter_dict.values():
			""" demande à l'utilisateur la valeur tant que 
			celle-ci n'est pas conforme """
			while not item.set_value(input(item.message)): pass
		return parameter_dict

	def load_tournament_page(self, tournament_list):
		os.system(CLEAN_SCREEN)
		print("Chargement d'un ancien tournois")
		i = 1
		for item in tournament_list:
			print(f"{i} : {item}")
			i +=1
		return user_choices("indiquer votre choix : ", range(1,i+1))

	def ask_to_create_tournament(self):
		print_message("vous devez créer un nouveau tournois avant d'ajouter des joueurs")		

	def not_implemented(self):
		print_message("cette fonction n'est pas encore implementée")

	def max_number_players_reach(self):
		print_message("vous avez atteint le nombre maximal de joueur dans cette partie")

	def database_not_found(self):
		print_message("aucune base de donnée trouvée")

	def issues_database(self, error = None):
		if error != None:
			print_message(f"Problème lors de l'importation de la base de donnée \
			 				\n erreur rencontré : {error}")
		else:
			print_message("Problème lors de l'importation de la base de donnée")

	def save_performed_page(self):
		print_message("Données sauvegardé")

	def error_save_page(self, error = None):
		if error != None:
			print_message(f"Echec de la sauvegarde des données \
			 				\n erreur rencontré : {error}")
		else : 
			print_message("Echec de la sauvegarde des données")

	def exit_message(self):
		os.system(CLEAN_SCREEN)
		print("Au revoir et bonne journée")


def print_message(text):
		os.system(CLEAN_SCREEN)
		print(text)
		os.system("pause")


def user_choices(text, range):
	input_wrong = True
	while input_wrong:
		user_input = input(text)
		if user_input.isnumeric(): 
			user_input = int(user_input)
		if user_input in range:
			input_wrong = False
	return user_input


if __name__ == "__main__":
	views_object = views()
	views_object.start_view()
	views_object.main_menu_view()