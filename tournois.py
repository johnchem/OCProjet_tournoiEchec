from datetime import datetime 


class tournois():
	'''
	_________________________
	name : str
	location : str
	date : datetime
	players : [persone]
	rounds : [round]
	time_control : ["bullet", "blitz", "coup rapide"] defaut : bullet
	nbr_of_round : int
	description : str
	'''
	def __init__(self, name, location, date, players, rounds, time_control = "bullet", nbr_de_tours  =4, description = ""):
		self.name = name
		self.location = location
		self.date = date
		self.nbr_of_round = nbr_of_round
		self.rounds = rounds
		self.players = players
		assert time_control in ["bullet", "blitz", "coup rapide", None], \
			"le temps est toujours contrôlé selon un bullet, un blitz ou un coup rapide"
		self.time_control = time_control
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
	def __init__(self, name, beginDateTime, endDateTime):
		self.name = name
		self.beginDateTime = datetime.now()
		self.match = []

	def addMatch(self, match):
		self.match.append(match)

	def endRound(self):
		self.endDateTime = datetime.now()


class match():
	'''
	_________________________
	score : ([joueur, int], [joueur, int])
	'''
	def __init__(self, player_1, score_player_1, player_2, score_player_2):
		self.player_1 = player_1
		self.player_2 = player_2
		self.score_player_1 = score_player_1
		self.score_player_2 = score_player_2
		
	def __str__(self):
		return f"{self.player_1.nom} {self.score_player_1} : {self.score_player_2} {self.player_2.nom}"

	def result(self):
		return ([self.joueur_1, self.score_joueur_1],
				[self.joueur_2, self.score_joueur_2])

