import copy # module to avoid modify the original testing data

#import function to test
from chess_tournament.controller.deserializer import deserialize_tournament, \
deserialize_player, deserialize_round, deserialize_match

#import model
from chess_tournament.models.date_property import DateProperty
from chess_tournament.models.gender_property import GenderProperty
from chess_tournament.models.property import Property
from chess_tournament.models.multiple_choices_property import MultipleChoicesProperty
from chess_tournament.models.tournament import Tournament, TournamentSwiss
from chess_tournament.models.player import Player
from chess_tournament.models.round import Round
from chess_tournament.models.match import Match

#import data for testing
from chess_tournament.unittest.test_data import *

def test_deserialize_player(players_serialized, player, text = ""):
	print(text)
	players_serialized = copy.deepcopy(players_serialized)
	output = deserialize_player(**players_serialized)
	assert output == player, \
	f"erreur lors de l'import d'un joueur \n {vars(output)} \n {vars(player)}"

def test_deserialize_match(match_serialized, match, text = ""):
	print(text)
	match_serialized = copy.deepcopy(match_serialized)
	output = deserialize_match(**match_serialized)
	assert output == match, \
	f"erreur lors de l'import d'un match \n {vars(output)}"

def test_deserialize_round(round_serialized, round, text = ""):
	print(text)
	round_serialized = copy.deepcopy(round_serialized)
	output = deserialize_round(**round_serialized)
	assert output == round, \
	f"erreur lors de l'import d'un round \n {vars(output)}"	

def test_deserialize_tournament(tournament_serialised, tournament, text = ""):
	print(text)
	tournament_serialised = copy.deepcopy(tournament_serialised)
	output = deserialize_tournament(**tournament_serialised)
	assert output == tournament, \
	f"erreur lors de l'import d'un tournois \n {vars(tournament)} \n {vars(output)}"

if __name__ == "__main__":
#def run_test_deserializer():
	list_test_player = [(serialized_player_1, player_1),
						(serialized_player_2, player_2),
						(serialized_player_3, player_3),
						(serialized_player_4, player_4),
						(serialized_player_5, player_5),
						(serialized_player_6, player_6),
						(serialized_player_7, player_7),
						(serialized_player_8, player_8)]

	list_test_match = [(serialized_match_1, match_1),
					   (serialized_match_2, match_2),
					   (serialized_match_3, match_3),
					   (serialized_match_4, match_4),
					   (serialized_match_5, match_5),
					   (serialized_match_6, match_6)]

	list_test_round = [(serialized_round_1, round_1),
					   (serialized_round_2, round_2)]

	list_test_tournament = [(serialised_tournament_1, tournament_1),
							(serialised_tournament_2, tournament_2)]

	i = 1
	print("_____test_deserialize_player______")
	for ser_player, player in list_test_player:
		test_deserialize_player(ser_player, player, f"player {i}")
		i += 1
	print("")

	i = 1
	print("_____test_deserialize_match______")
	for ser_match, match in list_test_match:
		test_deserialize_match(ser_match, match, f"match {i}")
		i += 1

	i = 1
	print("_____test_deserialize_round______")
	for ser_round, rnd in list_test_round:
		test_deserialize_round(ser_round, rnd, f"round {i}")
		i += 1

	i = 1
	print("_____test_deserialize_tournament______")
	for ser_tournament, tournament in list_test_tournament:
		test_deserialize_tournament(ser_tournament, tournament, 
			f"tournament {i}")
		i += 1

#if __name__ == "__main__":
#	run_test_deserializer()


