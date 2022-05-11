from chess_tournament.models.property import Property
from chess_tournament.models.date_property import DateProperty
from chess_tournament.models.gender_property import GenderProperty
import copy

class Player:
	""" gere le tranfert et le controle des valeurs au modele
	propriété pour le genre du joueur
	Force la valeur à être en majuscule 

	Attribut
	-----------
	name : str 
		nom du joueur
	forname : str
		prénom du joueur
	birth_date : datetime
		date de naissance du joueur 
	gender : str 
		sexe du joueur
	rank : int 
		classement du joueur 	

	Methodes
	-----------
	
	"""
	def __init__(self, name, forname, birth_date, gender, rank):
		self.name = name.value
		self.forname = forname.value
		self.birth_date = birth_date.value
		self.gender = gender.value
		self.rank = rank.value
		self.id = ""

	def add_opponent(self, player):
		self.opponent.append(player)

	def is_opponent_already_faced(self, player):
		return player in self.opponent

	def serialize(self):
		serialized_player = copy.deepcopy(vars(self))
		serialized_player["birth_date"] = serialized_player["birth_date"].strftime("%d/%m/%Y")
		return serialized_player

	def __repr__(self):
		return (f'{self.forname} {self.name} ({self.gender})'
				f' née le {self.birth_date.strftime("%d/%m/%Y")}'
				f' : {self.rank}'
				)

	def __eq__(self, other):
		if not isinstance(other, Player):
			# don't attempt to compare against unrelated types
			return NotImplemented
		list_compare = [self.name != other.name,
						self.forname != other.forname,
						self.birth_date != other.birth_date]
		# return false if any difference exist
		return not any(list_compare)

	def __enter__(self):
		return self

	def __exit__(self, *err):
		self.close()
		

if __name__ == "__main__":
	from datetime import datetime as dt
	name = Property("name")
	name.set_value("paul")
	forname = Property("forname")
	forname.set_value("michel")
	birth_date = DateProperty("birth_date")
	birth_date.set_value("01/01/2001")
	gender = GenderProperty("gender")
	gender.set_value("H")
	rank = Property("rank")
	rank.set_value(0)

	joueur = Player(name, forname, birth_date, gender, rank)
	print(vars(joueur))