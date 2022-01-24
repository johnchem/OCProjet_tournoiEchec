from datetime import datetime 


class tournois():
	def __init__(self, nom, lieu, date, nbr_de_tours, tournees = 4, joueurs, controle_du_temps, description = ""):
		self.nom = nom
		self.lieu = lieu
		self.date = date
		self.nbr_de_tours = nbr_de_tours
		self.tournees = tournees
		self.joueurs = joueurs
		assert controle_du_temps in ["bullet", "blitz", "coup rapide"], _
			"le temps est toujours contrôlé selon un bullet, un blitz ou un coup rapide"
		self.controle_du_temps = controle_du_temps
		self.description = description

class round():
	def __init__(self, nom, dateDebut, dateFin):
		self.nom = nom
		self.dateDebut = datetime.nom()
		self.match = []

	def addMatch(self, match):
		self.match.append(match)

