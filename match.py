class match():
	'''
	_________________________
	score : ([joueur, int], [joueur, int])
	'''
	def __init__(self, player_1, score_player_1, player_2, score_player_2):
		self.player_1 = player_1
		self.player_2 = player_2
		self.score_player_1 = score_player_1
		self.score_player_2 = score_player_2
		
	def __str__(self):
		return f"{self.player_1.nom} {self.score_player_1} : {self.score_player_2} {self.player_2.nom}"

	def result(self):
		return ([self.joueur_1, self.score_joueur_1],
				[self.joueur_2, self.score_joueur_2])