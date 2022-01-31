class Tournament():
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
	TIME_CONTROLE_STANDARD = ["bullet", "blitz", "coup rapide"]

	def __init__(self, name : str, location : str, date, 
						rounds : list, time_control, 
						  nbr_de_tours = 4, description = ""):
		self.name = name
		self.location = location
		self.date = date
		self.nbr_of_round = nbr_of_round
		self.rounds = rounds
		self.players = []
		
		assert time_control in TIME_CONTROLE_STANDARD, \
			"le temps est toujours contrôlé selon un bullet, un blitz ou un coup rapide"
		self.time_control = time_control
		self.description = description
		
		self.currentRound = 0

	def addPlayer(self, player):
		self.players.append(player)

	def isFull(self):
		if len(self.turnament.players) == 8:
			return True
		else : 
			return False

	def endRound(self):
		self.rounds[self.currentRound].endRound()
	
	def setResult(self):
		self.rounds[self.currentRound].setResult()

	def player_group_generation(self):
		pass
				
	def _backup(self):
		"""backup the players list and the """
		pass

class TournamentSwiss(Tournament):
	""" tournament with the swiss systeme """
	def player_group_generation(self):
		if len(self.players) < 8:
			return None
		else: 
			if self.currentRound == 1:
				pass
			else:
				pass