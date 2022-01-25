
class joueur():
	def __init__(self, name, forname, birth_date, sexe, rank = 0):
		self.name = name
		self.forname = forname
		self.birth_date = birth_date
		self.sexe = sexe
		self.rank = rank

	def __str__(self):
		return f"{self.forname} {self.name} ({self.sexe}) née le {self.birth_date} : {self.classement}"

