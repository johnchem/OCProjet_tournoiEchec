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
	def __init__(self, name : str, beginDateTime, endDateTime):
		self.name = name
		self.beginDateTime = datetime.now()
		self.endDateTime = endDateTime
		self.match = []
		self.done = False

	def addMatch(self, match):
		self.match.append(match)

	def endRound(self):
		self.endDateTime = datetime.now()
		self.done = True

	def getMatchList(self):
		pass

	def setResult(self):
		pass

	def serialize(self):
		serialized_round = vars(self)
		serialized_round["beginDateTime"] = serialized_round["beginDateTime"].strftime("%d/%m/%Y")
		serialized_round["endDateTime"] = serialized_round["endDateTime"].strftime("%d/%m/%Y")
		serialized_round["match"] = [x.serialize for x in self.match]
		return serialized_round