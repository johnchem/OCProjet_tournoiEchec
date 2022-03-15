
TIME_CONTROLE_STANDARD = ["bullet", "blitz", "coup rapide"]

class Tournament():
	'''
	_________________________
	name.value : str
	location.value : str
	date.value : datetime
	players.value : [persone]
	rounds : [round]
	time_control.value : ["bullet", "blitz", "coup rapide"]
	number_of_round.value : int
	description.value : str
	'''
	def __init__(self, *, name, location, 
						date,
						duration,
						time_control, 
						number_of_round = 4, 
						description = ""):
		self.name = name.value
		self.location = location.value
		self.date = date.value
		self.duration = duration.value
		self.number_of_round = number_of_round.value
		self.time_control = time_control.value
		self.rounds = []
		self.players = []
		self.time_control = time_control.value
		self.description = description.value
		self.currentRound = 0

	def addPlayer(self, player):
		"""add a new player in the tournament"""
		self.players.append(player)

	def isFull(self):
		""" check if there are 8 and no more players"""
		if len(self.players) >= 8:
			return True
		else : 
			return False

	def endRound(self):
		self.rounds[self.currentRound].endRound()
	
	def setResult(self):
		self.rounds[self.currentRound].setResult()

	def player_group_generation(self):
		pass
	
	def __str__(self):
		a = [f"Nom : {self.name}",
			f"Lieu : {self.location}",
			f"A partir du {self.date} pendant {self.duration} jours",
			f"{self.number_of_round} tours avec la régle {self.time_control}",
		]
		return "\n".join(a)

	def serialize(self):
		serialized_tournament = vars(self)
		serialized_tournament["date"] = serialized_tournament["date"].strftime("%d/%m/%Y")
		serialized_tournament["players"] = [x.serialize for x in self.players]
		return serialized_tournament

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

if __name__ == "__main__":
	pass