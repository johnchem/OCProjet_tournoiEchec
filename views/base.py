
import os
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
		user_answer = input("indiquer votre choix : ")
		return int(user_answer)

	def get_tournament_data(self):
		pass

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


if __name__ == "__main__":
	views_object = views()
	views_object.start_view()
	views_object.main_menu_view()
	pass