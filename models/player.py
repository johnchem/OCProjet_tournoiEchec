
class Player:
	def __init__(self, name, forname, birth_date, sexe, rank = 0):
		self.name = name
		self.forname = forname
		self.birth_date = birth_date
		self.sexe = sexe
		self.rank = rank
		self.opponents = []

	def add_opponent(self, player):
		self.opponent.append(player)

	def is_opponent_already_faced(self, player):
		return player in self.opponent

	def __str__(self):
		return f"{self.forname} {self.name} ({self.sexe}) née le {self.birth_date} : {self.classement}"


