class tournament():
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
	def __init__(self, name, location, date, rounds, time_control = "bullet", nbr_de_tours  =4, description = ""):
		self.name = name
		self.location = location
		self.date = date
		self.nbr_of_round = nbr_of_round
		self.rounds = rounds
		self.players = []
		assert time_control in ["bullet", "blitz", "coup rapide", None], \
			"le temps est toujours contrôlé selon un bullet, un blitz ou un coup rapide"
		self.time_control = time_control
		self.description = description

	def addPlayer(self, player):
		self.players.append(player)

	def isFull(self):
		if len(self.turnament.players) == 8:
			return True
		else : 
			return False

	def _backup(self):
		"""backup the players list and the """

		pass