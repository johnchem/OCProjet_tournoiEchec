class Match():
	'''
	_________________________
	score : ([joueur, int], [joueur, int])
	'''
	def __init__(self, player_1, player_2):
		self.player_1 = {"player": player_1,
						"score":None,
						"color":None}
		self.player_2 = {"player": player_2,
						"score":None,
						"color":None}
		
	def set_color(self):
		pass

	def result(self):
		return ([self.joueur_1, self.joueur_1["score"]],
				[self.joueur_2, self.joueur_2["score"]])

	def serialize(self):
		player_1 = self.player_1
		player_1["player"] = self.player_1["player"].serialize
		
		player_2 = self.player_2
		player_2["player"] = self.player_2["player"].serialize

		return {"player_1": player_1,
				"player_2": player_2}

	def __str__(self):
		return f'{self.player_1["player"].name} {self.player_1["score"]} : '+\
			   f'{self.player_2["score"]} {self.player_2["player"].name}'

	def __repr__(self):
		return (f'{self.player_1["player"].name} {self.player_1["score"]} : '
			   f'{self.player_2["score"]} {self.player_2["player"].name}'
			   )
	
	def __eq__(self, other):
		if not isinstance(other, Match):
			# don't attempt to compare against unrelated types
			return NotImplemented
		# compare player instance between them.
		player_1_eq_1 = self.player_1["player"] == other.player_1["player"]
		player_1_eq_2 = self.player_1["player"] == other.player_2["player"]
		player_2_eq_1 = self.player_2["player"] == other.player_1["player"]
		player_2_eq_2 = self.player_2["player"] == other.player_2["player"]

		if player_1_eq_1 and player_2_eq_2:
			''' compare self_player_1 with other_player_1 and  
			self_player_2 with other_player_2
			'''
			list_compare = [self.player_1["score"] != other.player_1["score"],
							self.player_2["score"] != other.player_2["score"],
							self.player_1["color"] != other.player_1["color"],
							self.player_2["color"] != other.player_2["color"]]
		elif player_1_eq_2 and player_2_eq_1:
			''' compare self_player_1 with other_player_2 and  
			self_player_2 with other_player_1
			'''
			list_compare = [self.player_1["score"] != other.player_2["score"],
							self.player_2["score"] != other.player_1["score"],
							self.player_1["color"] != other.player_2["color"],
							self.player_2["color"] != other.player_1["color"]]
		else:
			return False
		# return false if any difference exist
		return not any(list_compare)