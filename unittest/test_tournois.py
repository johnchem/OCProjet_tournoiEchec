from chess_tournament.models.tournament import Tournament
#from models.tournament import TournamentSwiss
from chess_tournament.models.player import Player
import random

def test_tournois():
	pass

def test_round():
	pass

def create_round(tournament, round_nb):
	tournament.player_group_generation()
	assert is tournament.round, "truc" 
	for match in tournament.round[round_nb]:
		print(match)

def test_match(liste_joueur):
	liste_match = []
	liste_score = [0, 1, 0.5]
	for i in range(1,9):
		(joueur1, joueur2) = random.choices(liste_joueur, k=2)
		(score1, score2) = random.choices(liste_score, k=2)
		liste_match.append(tournois.match(joueur1, score1, joueur2, score2))
	[print(x) for x in liste_match]
	pass

if __name__ == "__main__":
	tournament_data = {"name" : "test", 
						"location" : "nantes", 
						"date" : "15Jan2021",
						"duration" :  "1",
						"time_control" : "blitz", 
						"number_of_round" : 5, 
						"description" : ""}

	nvxJoueur = [("Tardiff", "Stephanie", "26/09/1967", "F", 15),
				("Connie", "Lam", "10/06/1986", "F", 12),
				("Cleveland","Noon","03/11/1938","M", 5),
				("Disalvo","Aaron","13/09/1967","M", 65),
				("Digiacomo","David","13/09/1944","M", 41),
				("Adela","Scanlon","10/01/1951","F", 11),
				("Galbraith","Rosemary","03/11/1970","F", 8),
				("Burroughs","Eric","03/09/1967","M",3)]
	
	tournois = TournamentSwiss(**tournament_data)
	liste_joueur = []
	for nom, prenom, date_de_naissance, sexe, classement in nvxJoueur:
		liste_joueur.append(
			joueur.joueur(nom, prenom, date_de_naissance, sexe, classement)
			)

	test_match(liste_joueur)

	pass