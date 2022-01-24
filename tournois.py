from datetime import datetime 


class tournois():
	'''
	_________________________
	nom : str
	lieu : str
	date : datetime
	joueurs : [persone]
	tournees : [round]
	controle_du_temps : ["bullet", "blitz", "coup rapide"] defaut : bullet
	nbr_de_tours : int
	description : str
	'''
	def __init__(self, nom, lieu, date, joueurs, tournees, controle_du_temps = "bullet", nbr_de_tours  =4, description = ""):
		self.nom = nom
		self.lieu = lieu
		self.date = date
		self.nbr_de_tours = nbr_de_tours
		self.tournees = tournees
		self.joueurs = joueurs
		assert controle_du_temps in ["bullet", "blitz", "coup rapide", None], \
			"le temps est toujours contrôlé selon un bullet, un blitz ou un coup rapide"
		self.controle_du_temps = controle_du_temps
		self.description = description


class round():
	'''
	_________________________
	nom : str
	dataDebut : datetime
	dateFin : datetime
	match : [match]

	-------------------------
	.addMatch(match) -> None
	'''
	def __init__(self, nom, dateDebut, dateFin):
		self.nom = nom
		self.dateDebut = datetime.nom()
		self.match = []

	def addMatch(self, match):
		self.match.append(match)


class match():
	'''
	_________________________
	score : ([joueur, int], [joueur, int])
	'''
	def __init__(self, joueur_1, score_joueur_1, joueur_2, score_joueur_2):
		self.score_final = ([joueur_1, score_joueur_1],
							[joueur_2, score_joueur_2])

	

