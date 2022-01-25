import tournois
import joueur
import random

def test_tournois():
	pass

def test_round():
	pass

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
	nvxJoueur = [("Tardiff", "Stephanie", "26/09/1967", "F"),
				("Connie", "Lam", "10/06/1986", "F"),
				("Cleveland","Noon","03/11/1938","M"),
				("Disalvo","Aaron","13/09/1967","M"),
				("Digiacomo","David","13/09/1944","M"),
				("Adela","Scanlon","10/01/1951","F"),
				("Galbraith","Rosemary","03/11/1970","F"),
				("Burroughs","Eric","03/09/1967","M")]
	
	liste_joueur = []
	for nom, prenom, date_de_naissance, sexe in nvxJoueur:
		liste_joueur.append(
			joueur.joueur(nom, prenom, date_de_naissance, sexe)
			)

	test_match(liste_joueur)

	pass