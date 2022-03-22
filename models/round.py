from datetime import datetime

class Round():
	'''
	_________________________
	nom : str
	dataDebut : datetime
	dateFin : datetime
	match : [match]

	-------------------------
	.addMatch(match) -> None
	'''
	def __init__(self, name : str):
		self.name = name
		self.begin_date_time = datetime.now()
		self.end_date_time = None
		self.match = []
		self.is_done = False

	def addMatch(self, match):
		self.match.append(match)

	def endRound(self):
		self.end_date_time = datetime.now()
		self.is_done = True

	def getMatchList(self):
		pass

	def setResult(self):
		pass

	def serialize(self):
		serialized_round = vars(self)
		serialized_round["begin_date_time"] = serialized_round["begin_date_time"].strftime("%d/%m/%Y %X")
		serialized_round["end_date_time"] = serialized_round["end_date_time"].strftime("%d/%m/%Y %X")
		serialized_round["match"] = [x.serialize for x in self.match]
		return serialized_round