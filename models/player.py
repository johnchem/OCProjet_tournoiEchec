
class Player:
	def __init__(self, name, forname, birth_date, gender, rank = 0):
		self.name = name.value
		self.forname = forname.value
		self.birth_date = birth_date.value
		self.gender = gender.value
		self.rank = rank.value
		self.opponents = []

	def add_opponent(self, player):
		self.opponent.append(player)

	def is_opponent_already_faced(self, player):
		return player in self.opponent

	def __str__(self):
		return f"{self.forname} {self.name} ({self.gender}) née le {self.birth_date} : {self.classement}"


