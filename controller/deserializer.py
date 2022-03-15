from chess_tournament.models.property import Property
from chess_tournament.models.date_property import DateProperty
from chess_tournament.models.multiple_choices_property import MultipleChoicesProperty
from chess_tournament.models.tournament import TournamentSwiss

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
	number_of_round.set_value(kwargs["number_of_round"])

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

	tournament.currentRound = kwargs["currentRound"]
	tournament.round = kwargs["rounds"]
	tournament.players = kwargs["players"]
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
	rank.set_value(kwargs["forname"])
	
	player = Player(name, forname, birth_date, gender, rank)

	player.opponents = kwargs["opponents"]
	
	return player

def deserialize_round(**kwargs):
	name = Property()
	name.set_value(kwargs["name"])

	restored_round = Round(name)

	begin_date_time = datetime.strptime(kwargs["begin_date_time"], "%d/%m/%Y %X")
	restored_round.begin_date_time = begin_date_time 

	end_date_time = datetime.strptime(kwargs["end_date_time"], "%d/%m/%Y %X")
	restored_round.end_date_time = end_date_time

	end_round = kwargs["done"]
	match = [deserialize_match(x) for x in kwargs["match"]]
