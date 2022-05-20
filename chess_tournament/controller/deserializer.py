#import modole
from binascii import a2b_hex
from datetime import datetime

from chess_tournament.models.property import Property
from chess_tournament.models.date_property import DateProperty
from chess_tournament.models.multiple_choices_property import MultipleChoicesProperty
from chess_tournament.models.tournament import TournamentSwiss
from chess_tournament.models.match import Match
from chess_tournament.models.round import Round
from chess_tournament.models.player import Player

from chess_tournament.models.gender_property import GenderProperty


def deserialize_tournament(**kwargs):
	name = Property()
	name.set_value(kwargs["name"])
	
	location = Property()
	location.set_value(kwargs["location"])
	
	date = DateProperty()
	date.set_value(kwargs["date"])
	
	duration = Property()
	duration.set_value(kwargs["duration"])
	
	number_of_round = Property()
	number_of_round.set_value(int(kwargs["number_of_round"]))

	time_control = MultipleChoicesProperty()
	time_control._set_value(kwargs["time_control"])

	description = Property()
	description.set_value(kwargs["description"])

	tournament = TournamentSwiss(name = name, 
			date = date,
			duration = duration,
			number_of_round = number_of_round,
			description = description,
			location = location,
			time_control = time_control)

	tournament.current_round = int(kwargs["current_round"])
	tournament.rounds = [deserialize_round(**x) for x in kwargs["rounds"]]
	tournament.players = [deserialize_player(**x) for x in kwargs["players"]]

	if "id" in kwargs:
		tournament.id = kwargs["id"]
	
	return tournament

def deserialize_player(**kwargs):
	name = Property()
	name.set_value(kwargs["name"])
	
	forname = Property()
	forname.set_value(kwargs["forname"])
	
	birth_date = DateProperty()
	birth_date.set_value(kwargs["birth_date"])
	
	gender = Property()
	gender.set_value(kwargs["gender"])
	
	rank = Property()
	rank.set_value(kwargs["rank"])
	
	player = Player(name, forname, birth_date, gender, rank)

	if "id" in kwargs:
		player.id = kwargs["id"]
	
	return player

def deserialize_round(**kwargs):
	name = kwargs["name"]

	restored_round = Round(name)

	begin_date_time = datetime.strptime(kwargs["begin_date_time"], "%d/%m/%Y %X")
	restored_round.begin_date_time = begin_date_time 

	if "end_date_time" in kwargs:
		end_date_time = datetime.strptime(kwargs["end_date_time"], "%d/%m/%Y %X")
		restored_round.end_date_time = end_date_time

	round_is_done = kwargs["is_done"]
	restored_round.is_done = round_is_done

	match = [deserialize_match(**x) for x in kwargs["match"]]
	restored_round.match = match

	return restored_round

def deserialize_match(**kwargs):
	dict_player_1 = kwargs["player_1"]
	dict_player_1["player"] = deserialize_player(**dict_player_1["player"])

	dict_player_2 = kwargs["player_2"]
	dict_player_2["player"] = deserialize_player(**dict_player_2["player"])

	restored_match = Match(dict_player_1["player"], dict_player_2["player"])
	restored_match.player_1 = dict_player_1
	restored_match.player_2 = dict_player_2

	return restored_match
