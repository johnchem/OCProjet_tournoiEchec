class Match():
	'''
	_________________________
	score : ([joueur, int], [joueur, int])
	'''
	def __init__(self, player_1, player_2):
		self.player_1 = {"player":player_1,
						"score":None,
						"color":None}
		self.player_2 = {"player":player_2,
						"score":None,
						"color":None}
		
	def __str__(self):
		return f"{self.player_1.player.nom} {self.score_player_1} : {self.score_player_2} {self.player_2.nom}"

	def set_color(self):
		pass

	def result(self):
		return ([self.joueur_1, self.score_joueur_1],
				[self.joueur_2, self.score_joueur_2])