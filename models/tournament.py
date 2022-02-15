
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
		
		assert time_control.value in TIME_CONTROLE_STANDARD, \
			f"le temps est toujours contrôlé selon un bullet, un blitz ou un coup rapide. recu : {time_control}"
		self.time_control = time_control.value
		self.description = description
		
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

				
	def _backup(self):
		"""backup the players list and the """
		pass

	def __str__(self):
		a = [f"Nom : {self.name}",
			f"Lieu : {self.location}",
			f"A partir du {self.date} pendant {self.duration} jours",
			f"{self.number_of_round} tours avec la régle {self.time_control}",
		]
		return "\n".join(a)

	def serialize(self):
		return vars(self)

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
	mockData1 = {
	"name" : "riri",
	"location" : "paris",
	"date" : "15Feb2022",
	"duration" : "2",
	"time_control" : "blitz",
	"number_of_round" : 5,
	"description" : ""
	}

	mockData2 : {
	"name" : "loulou",
	"location" : "nantes",
	"date" : "30Mar2022",
	"duration" : "1",
	"time_control" : "coup rapide",
	"number_of_round" : 4,
	"description" : ""
	}

	tour = Tournament(**mockData1)
	print(tour)
	swisTour = TournamentSwiss(**mockData1)
	print(swisTour)