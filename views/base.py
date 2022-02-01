
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
		input("---- appuyer sur 'Enter' pour continuer ----")
		os.system(CLEAN_SCREEN)
		pass

	def main_menu_page(self, menu_item_list):
		i = 1
		print("________MENU PRINCIPAL________")
		for menu_item in menu_item_list:
			print(f"{i} : {menu_item}")
			i +=1
		return user_choices("indiquer votre choix : ", range(1,i+1))
		
	def get_tournament_data(self):
		os.system(CLEAN_SCREEN)
		value_dict = {}
		print("CREATION D UN NOUVEAU TOURNOI")
		print("Veuillez remplir les champs ci-dessous \n")
		value_dict["name"] = input("Nom : ")
		value_dict["location"] = input("Lieu : ")
		value_dict["date"] = input("Date : ")
		value_dict["duration"] = input("Durée : ")
		round_nbr = input("Nombre de tours (defaut 4) : ")
		if round_nbr == "":
			value_dict["number_of_round"] = round_nbr
		print("Quel gestion du temps voullez vous appliquer ? :")
		print("1: Bullet   2: Blitz   3: Coup rapide")
		time_control_choices = user_choices("Choix : ", range(1,4))-1
		value_dict["time_control"] = TIME_CONTROLE_STANDARD[time_control_choices]
		value_dict["description"] = input("Desciption : \n")
		return value_dict

	def create_tournament(self):
		pass

	def new_player(self):
		pass

	def max_number_players_reach(self):
		pass

	def not_implemented(self):
		print("cette fonction n'est pas encore implementée")

	def exit_message(self):
		os.system(CLEAN_SCREEN)
		print("Au revoir et bonne journée")

def user_choices(text, range):
	input_conform = False
	while not input_conform:
		user_input = input(text)
		if user_input.isnumeric() : user_input = int(user_input)
		if user_input in range:
			input_conform = True
	return user_input


if __name__ == "__main__":
	views_object = views()
	views_object.start_view()
	views_object.main_menu_view()