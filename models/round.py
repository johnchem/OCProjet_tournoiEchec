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
	
	def __repr__(self):
		if self.is_done:
			return (f'{self.name}'
				f' le {self.begin_date_time.strftime("%d/%m/%Y")}'
				f' entre {self.begin_date_time.strftime("%X")}'
				f' et {self.end_date_time.strftime("%X")}'
				)
		else:
			return (f'{self.name}'
				f' le {self.begin_date_time.strftime("%d/%m/%Y")}'
				f' en cours depuis {self.begin_date_time.strftime("%X")}'
				)

	def __eq__(self, other):
		if not isinstance(other, Round):
			# don't attempt to compare against unrelated types
			return NotImplemented
		''' compare the different matchs
		store true in a list is a match is not found
		'''
		match_compare = []
		for x in self.match:
			match_not_found = True
			for y in other.match:
				if x == y :	match_not_found = False
			match_compare.append(result)

		list_compare = [self.name != other.name,
					    self.begin_date_time != other.begin_date_time,
					    self.end_date_time != other.end_date_time,
					    *match_compare]
		#return false if any difference exist between self and other
		return not any(list_compare)