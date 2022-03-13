import pathlib
from chess_tournament.controller.db_manager import load_tournament_data

# controle la présence d'une base de données
		
def test_list_tournament(DB_ADDRESS):
	if DB_ADDRESS.exists():
		print(DB_ADDRESS)
		# chargement de l'ensemble des tournois enregistré
		history_tournament = load_tournament_data(DB_ADDRESS)
		# gestion de la reception d'erreur lors de l'importation de la db
		#print(history_tournament)
		if isinstance(history_tournament, list):
			# mise en forme et affichage les tournois sauvegardés
			tournament_name_formated = tournament_historic(history_tournament)
			print(tournament_name_formated)
		else :
			print("probleme avec l'importation des données")
	else : 
		print("fichier de la base de donnée non trouvé")
		

def tournament_historic(tournament_list):
		output_list = []
		for tournament in tournament_list:
			name = tournament["name"]
			output_list.append(f"{tournament["name"]}")
		return output_list


if __name__ == "__main__":
	DB_ADDRESS = pathlib.Path(__file__).parent.absolute().joinpath("DB_unitest.json")
	test_list_tournament(DB_ADDRESS)
	pass