
class joueur():
	def __init__(self, nom, prenom, date_de_naissance, sexe, classement = 0):
		self.nom = nom
		self.prenom = prenom
		self.date_de_naissance = date_de_naissance
		self.sexe = sexe
		self.classement = classement

	def __repr__(self):
		return f"{self.prenom} {self.nom} ({self.sexe}) née le {self.date_de_naissance} : {self.classement}"

