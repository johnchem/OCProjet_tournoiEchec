from math import trunc
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
		self.description = description.value
		self.current_round = 1
		self.dict_opponent = {}
		self.dict_score = {}

	def add_player(self, player):
		"""add a new player in the tournament"""
		self.players.append(player)
		# add the player in the tracking dict.
		self.dict_score[player.name] = 0
		self.dict_opponent[player.name] = []

	def is_full(self):
		""" check if there are 8 and no more players"""
		if len(self.players) >= 8:
			return True
		else : 
			return False

	def start_new_round(self, round):
		self.rounds.append(Round)
		self.current_round += 1	


	def end_round(self):
		self.rounds[self.current_round].end_round()

	def set_result(self):
		self.rounds[self.current_round].set_result()

	def player_group_generation(self):
		""" not implemented from standart tournament"""
		pass

	def get_players_opponent(self):
		tmp_list = []
		for round_played in self.round:
			tmp_list.append(round_played.get_players_opponent())

		for player, opponent in tmp_list:
			if player in self.dict_opponent:
				self.dict_opponent[player].append(opponent)
			else :
				self.dict_opponent[player] = [opponent]

	def get_players_score(self):
		tmp_list = []
		for round_played in self.round:
			tmp_list.append(round_played.get_players_score())

		for player, score in tmp_list:
			if player in self.dict_score:
				self.dict_score[player] += score
			else:
				self.dict_score[player] = score
	
	def serialize(self):
		serialized_tournament = vars(self)
		serialized_tournament["date"] = serialized_tournament["date"].strftime("%d/%m/%Y")
		serialized_tournament["players"] = [x.serialize for x in self.players]
		return serialized_tournament

	def __str__(self):
		a = [f"Nom : {self.name}",
			f"Lieu : {self.location}",
			f"A partir du {self.date} pendant {self.duration} jours",
			f"{self.number_of_round} tours avec la régle {self.time_control}",
		]
		return "\n".join(a)

	def __eq__(self, other):
		if not isinstance(other, type(self)):
			# don't attempt to compare against unrelated types
			return NotImplemented
		
		'''
		compare the rounda, as there are ordered, 
		they can be compare side to side
		'''
		for x, y in zip(self.rounds, other.rounds):
			if x != y : return False

		''' 
		iterate through the players list and record if 
		they are a match or not
		'''
		player_compare = []
		for x in self.players:
			player_not_found = True
			for y in other.players:
				if x == y : player_not_found = False
			player_compare.append(player_not_found)
		
		list_compare = [self.name != other.name,
						self.location != other.location,
						self.date != other.date,
						self.duration != other.duration,
						self.number_of_round != other.number_of_round,
						self.time_control != other.time_control,
						*player_compare,
						self.description != other.description,
						self.current_round != other.current_round]
		# return False if any difference exist between self and other
		return not any(list_compare)

class TournamentSwiss(Tournament):
	""" tournament with the swiss systeme """
	
	def player_group_generation(self):
		if len(self.players) < 8:
			return None
		else: 
			if self.current_round == 1:
				#sort the player
				list_players_sorted = sorted(self.players, key=lambda x : x.rank)
				#define the middle of the list, which also the number of matches
				nbr_match = trunc(len(list_players_sorted)/2)
				#split the list in two
				upper_half = list_players_sorted[:nbr_match]
				bottom_half = list_players_sorted[nbr_match:]

				return zip(upper_half, bottom_half)
			else:
				sort_function = lambda x : x.rank
				pass


if __name__ == "__main__":
	pass