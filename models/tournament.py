
TIME_CONTROLE_STANDARD = ["bullet", "blitz", "coup rapide"]

class Tournament():
	'''
	_________________________
	name : str
	location : str
	date : datetime
	players : [persone]
	rounds : [round]
	time_control : ["bullet", "blitz", "coup rapide"]
	nbr_of_round : int
	description : str
	'''
	def __init__(self, *, name : str, location : str, 
						date,
						duration,
						time_control : str, 
						number_of_round = 4, 
						description = ""):
		self.name = name
		self.location = location
		self.date = date
		self.duration = duration
		self.number_of_round = number_of_round
		self.rounds = []
		self.players = []
		
		assert time_control in TIME_CONTROLE_STANDARD, \
			"le temps est toujours contrôlé selon un bullet, un blitz ou un coup rapide"
		self.time_control = time_control
		self.description = description
		
		self.currentRound = 0

	def addPlayer(self, player):
		"""add a new player in the tournament"""
		self.players.append(player)

	def isFull(self):
		""" check if there are 8 and no more players"""
		if len(self.tournament.players) >= 8:
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
	def __init__(self, *, name : str, location : str, date,
						duration, time_control : str, 
						number_of_round = 4, description = ""):
		super().__init__(name = name, 
						location = location, 
						date = date, 
						duration = duration, 
						time_control = time_control,
						number_of_round = number_of_round, 
						description = description)
	
	def player_group_generation(self):
		if len(self.players) < 8:
			return None
		else: 
			if self.currentRound == 1:
				pass
			else:
				pass